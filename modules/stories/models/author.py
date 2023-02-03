from django.db import models
from django.conf import settings
from modules.stories.models.include import (
    idModel,
    statusModel,
    timeStampModel,
)


class Author(idModel, statusModel, timeStampModel):
    story = models.ForeignKey(
        "Stories",
        related_name="author_stories",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="author_user",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{} Written by {}".format(self.story.title, self.user.name())

    class Meta:
        verbose_name_plural = "authors"
        # app_label = "modules_stories"
