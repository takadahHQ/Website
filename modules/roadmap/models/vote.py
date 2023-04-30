from django.db import models
from modules.roadmap.models.feature import Feature
from modules.subscriptions.models.include import statusModel
import datetime


def expire():
    return datetime.datetime.today() + datetime.timedelta(days=30)


class Vote(statusModel):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name="votes")
    vote = models.BooleanField(default=True)  # True = upvote, False = downvote

    def __str__(self):
        return f"{ self.feature.title } - { self.user.username}"

    class Meta:
        verbose_name_plural = "Votes"
        app_label = "roadmap"
