from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
from modules.stories import images as img
from django.core.files import File
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager

from flag.models import Flag
from modules.stories.models.include import (
    idModel,
    timeStampModel,
)
from modules.stories.models import History


class Stories(idModel, timeStampModel):
    status_choices = (
        ("abandoned", "Abandoned"),
        ("complete", "Complete"),
        ("haitus", "Haitus"),
        ("prerelease", "Pre-Released"),
        ("published", "Published"),
        ("oneshot", "One Shot"),
        ("ongoing", "Ongoing"),
        ("draft", "Draft"),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, unique=True)
    abbreviation = models.CharField(max_length=15, unique=True)
    summary = RichTextField("synopsis")
    cover = models.ImageField(max_length=255, blank=True, null=True)
    story_type = models.ForeignKey("Type", on_delete=models.CASCADE)
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="story_followers",
        symmetrical=False,
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="story_likes"
    )
    dislikes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="story_dislike"
    )
    author = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="Author", related_name="authors", blank=True
    )
    editor = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="Editor", related_name="editors", blank=True
    )
    language = models.ForeignKey("Language", on_delete=models.CASCADE)
    genre = models.ManyToManyField("Genre", blank=True)
    characters = models.ManyToManyField("Character", related_name="names", blank=True)
    rating = models.ForeignKey(
        "Rating", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    released_at = models.DateTimeField()
    featured = models.BooleanField(default=False)
    featured_at = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()
    flags = GenericRelation(Flag)
    status = models.CharField(max_length=100, choices=status_choices, default="draft")

    def __str__(self):
        return self.title

    # @admin.display(description='Following')
    def following_count(self):
        return self.following.count()

    # .display(description='Follower')
    def followers_count(self):
        return self.followers.count()

    # #@admin.display(description='Likes')
    def likes_count(self):
        return self.likes.count()

    # #@admin.display(description='Dislikes')
    def dislikes_count(self):
        return self.dislikes.count()

    # #@admin.display(description='First chapter of Story')
    def get_read_guest(self):
        # hack to get it to work
        if self.chapters.first():
            return self.chapters.first().get_absolute_url()

    def get_read_user(self, request):
        story = History.objects.filter(user=request.user).get(story=self.story)
        return story.chapter.get_absolute_url()

    def create_cover(self):
        name = self.author.first().name()
        file = img.make(name, self.title, self.slug)
        filename = self.slug + ".png"
        self.cover.save(filename, File(file), save=True)
        return self.cover

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify("-".join([self.abbreviation, self.title]))
        # if not self.cover:
        #     self.cover = self.create_cover()

        super(Stories, self).save(*args, **kwargs)

    def get_cover(self):
        if not self.cover:
            self.cover = self.create_cover()
            return self.cover.url
        else:
            return self.cover.url

    def get_absolute_url(self):
        story_type = self.story_type.slug
        return reverse(
            "stories:show",
            kwargs={"type": story_type, "slug": self.slug},
        )

    class Meta:
        verbose_name_plural = "stories"
        app_label = "stories"
