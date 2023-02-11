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


class Categories(CacheInvalidationMixin, Sluggable, idModel, nameModel, statusModel, timeStampModel):
    category_type = models.ForeignKey(
        "Type", on_delete=models.CASCADE, blank=True, null=True
    )
    objects = CachedQueryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"
        # app_label = "modules_stories"
