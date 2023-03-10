from django.db import models
from django.conf import settings
from modules.core.models.include import (
    idModel,
    nameModel,
    statusModel,
    timeStampModel,
    CacheInvalidationMixin,
    CachedQueryManager,
)


class Languages(
    CacheInvalidationMixin, idModel, nameModel, statusModel, timeStampModel
):
    code = models.CharField(max_length=255)
    native_name = models.CharField(max_length=255)
    objects = CachedQueryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "languages"
        app_label = "core"
