from django.db import models
from modules.subscriptions.models.include import statusModel


class Feature(statusModel):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def get_votes(self):
        return self.get_upvotes() - self.get_downvotes()

    def get_downvotes(self):
        return self.votes.filter(vote=False).count()

    def get_upvotes(self):
        return self.votes.filter(vote=True).count()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Features"
        app_label = "roadmap"
