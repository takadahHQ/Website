from django.db import models
from django.conf import settings

from modules.stories.models.include import (
    Sluggable,
    idModel,
    statusModel,
    timeStampModel,
    CacheInvalidationMixin,
    CachedQueryManager,
)
from modules.stories.models.history import History


class Bookmark(CacheInvalidationMixin, idModel, statusModel, timeStampModel):
    story = models.ForeignKey(
        "Stories", related_name="bookmarked", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    url = models.CharField(max_length=255, blank=True, null=True)
    objects = CachedQueryManager()

    def __str__(self):
        return self.story.title

    def get_read_position(self):
        story = History.objects.get(story=self.story, user=self.user)
        return story.chapter.position

    def get_read(self):
        story = History.objects.get(story=self.story, user=self.user)
        return story.chapter.get_absolute_url()

    class Meta:
        verbose_name_plural = "bookmarks"
        app_label = "stories"
