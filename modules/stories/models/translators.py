from django.db import models
from django.conf import settings
from modules.stories.models.include import (
    idModel,
    statusModel,
    timeStampModel,
    CacheInvalidationMixin,
    CachedQueryManager,
)


class Translator(CacheInvalidationMixin, idModel, statusModel, timeStampModel):
    story = models.ForeignKey(
        "Stories",
        related_name="translator_stories",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="translator_user",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    objects = CachedQueryManager()

    def __str__(self):
        return "{} Translated by {}".format(self.story.title, self.user.name())

    class Meta:
        verbose_name_plural = "translators"
        app_label = "stories"
