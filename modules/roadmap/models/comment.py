from django.conf import settings
from django.db import models
from modules.roadmap.models.feature import Feature
from modules.subscriptions.models.include import statusModel
import datetime


def expire():
    return datetime.datetime.today() + datetime.timedelta(days=30)


class Comment(statusModel):
    feature = models.ForeignKey(
        Feature, on_delete=models.CASCADE, related_name="comments"
    )
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )
    content = models.TextField()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Comments"
        app_label = "roadmap"
