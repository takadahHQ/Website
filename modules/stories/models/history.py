from django.conf import settings
from django.db import models
from modules.stories.models.include import (
    Sluggable,
    idModel,
    nameModel,
    statusModel,
    timeStampModel,
)


class History(idModel, statusModel, timeStampModel):
    story = models.ForeignKey(
        "Stories", related_name="history", on_delete=models.CASCADE
    )
    chapter = models.ForeignKey(
        "Chapter", related_name="chapter", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.story.title

    class Meta:
        verbose_name_plural = "histories"
        app_label = "stories"
