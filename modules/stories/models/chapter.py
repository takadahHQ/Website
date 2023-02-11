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
    CacheInvalidationMixin
)


class Chapter(CacheInvalidationMixin ,idModel, statusModel, timeStampModel):
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
        try:
            next_post = Chapter.objects.get(pk=self.pk).filter(
                position=self.position + 1
            )
            return reverse(
                "stories:read",
                kwargs={
                    "type": next_post.story.story_type.slug,
                    "story": next_post.story.slug,
                    "slug": next_post.slug,
                },
            )
        except:
            return None

    def get_previous(self):
        try:
            previous_post = Chapter.objects.get(pk=self.pk).filter(
                position=self.position - 1
            )
            return reverse(
                "stories:read",
                kwargs={
                    "type": previous_post.story.story_type.slug,
                    "story": previous_post.story.slug,
                    "slug": previous_post.slug,
                },
            )
        except:
            return None

    def get_reviews(self):
        return self.reviews.filter(parent=None).filter(status="active")

    class Meta:
        verbose_name_plural = "chapters"
        # app_label = "modules_stories"
