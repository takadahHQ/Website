from django.db import models
from modules.stories.models.include import (
    Sluggable,
    idModel,
    nameModel,
    statusModel,
    timeStampModel,
    CacheInvalidationMixin,
    CachedQueryManager,
)


class Character(CacheInvalidationMixin, Sluggable, idModel, nameModel, statusModel, timeStampModel):
    story = models.ForeignKey(
        "Stories", related_name="story", on_delete=models.CASCADE, null=True, blank=True
    )
    category = models.ForeignKey(
        "Categories",
        related_name="category",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    objects = CachedQueryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "characters"
        # app_label = "modules_stories"
