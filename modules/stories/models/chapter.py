from django.db import models
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericRelation

from flag.models import Flag
from modules.stories.models.include import (
    idModel,
    statusModel,
    timeStampModel,
    CachedQueryManager,
    CacheInvalidationMixin,
)

from modules.subscriptions.models import Sponsors, Packages
from django.urls import reverse
from django.utils import timezone


class Chapter(CacheInvalidationMixin, idModel, statusModel, timeStampModel):
    story = models.ForeignKey(
        "Stories", related_name="chapters", on_delete=models.CASCADE
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    edited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="chapter_editor",
        on_delete=models.DO_NOTHING,
    )
    position = models.IntegerField()
    slug = models.SlugField(null=True, unique=True)
    title = models.CharField(max_length=255)
    text = RichTextUploadingField()
    authors_note = RichTextField(blank=True, null=True)
    words = models.IntegerField(blank=True, null=True)
    released_at = models.DateTimeField()
    flags = GenericRelation(Flag)

    objects = CachedQueryManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                self.story.abbreviation + "- chapter-" + f"{self.position}"
            )
            self.words = self.text.count(self.text)
        self.words = self.text.count(self.text)
        super(Chapter, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "stories:read",
            kwargs={
                "type": self.story.story_type.slug,
                "story": self.story.slug,
                "slug": self.slug,
            },
        )

    def get_next(self):
        previous_chapter, next_chapter = self.get_previous_and_next_chapters()
        if next_chapter:
            return next_chapter.get_absolute_url()
        else:
            return None

    def get_previous(self):
        previous_chapter, next_chapter = self.get_previous_and_next_chapters()
        if previous_chapter:
            return previous_chapter.get_absolute_url()
        else:
            return None

    def can_view(self, user=None):
        try:
            value = (
                Sponsors.objects.filter(user=user, package__story=self.story)
                .latest("created_at")
                .values()
            )
            sponsor = Sponsors.objects.get(id=value.id)
            package = Packages.objects.get(story=self.story, name=sponsor.package.name)
        except (Sponsors.DoesNotExist, Packages.DoesNotExist):
            return self.released_at <= timezone.now()

        # Get all the released chapters for this story
        released_chapters = Chapter.objects.filter(
            story=self.story, status="active", released_at__lte=timezone.now()
        ).order_by("position")

        # Get the position of the chapter in the list of released chapters
        position = released_chapters.values_list("position", flat=True).index(
            self.position
        )

        return position < package.advance or self.released_at <= timezone.now()

    def is_last(self):
        # Get all the released chapters for this story
        released_chapters = Chapter.objects.filter(
            story=self.story, status="active", released_at__lte=timezone.now()
        ).order_by("position")
        # get the latest chapter that has been released
        last_released = released_chapters.latest("position")

        # Get the position of the chapter in the list of released chapters
        # position = released_chapters.values_list("position", flat=True).index(
        #     self.position
        # )
        positions = released_chapters.values_list("position", flat=True)
        position = list(positions).index(self.position)

        return position == last_released.position

    def get_previous_and_next_chapters(self, user=None):
        # Prefetch all released chapters for this story
        released_chapters = (
            Chapter.objects.filter(
                story=self.story, status="active", released_at__lte=timezone.now()
            ).order_by("position")
            # .prefetch_related("user")
        )

        chapter_positions = released_chapters.values_list("position", flat=True)
        try:
            chapter_index = list(chapter_positions).index(self.position)
        except ValueError:
            return None, None

        if chapter_index > 0:
            previous_chapter = released_chapters[chapter_index - 1]
            if not previous_chapter.can_view(user=user):
                previous_chapter = None
        else:
            previous_chapter = None

        if chapter_index < len(released_chapters) - 1:
            next_chapter = released_chapters[chapter_index + 1]
            if not next_chapter.can_view(user=user):
                next_chapter = None
        else:
            next_chapter = None

        return previous_chapter, next_chapter

    def get_reviews(self):
        return self.reviews.filter(parent=None).filter(status="active")

    class Meta:
        verbose_name_plural = "chapters"
        # app_label = "modules_stories"
