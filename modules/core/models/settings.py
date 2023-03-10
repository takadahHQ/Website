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


class Settings(CacheInvalidationMixin, idModel, nameModel, statusModel, timeStampModel):
    tagline = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    footer = models.CharField(max_length=255)
    objects = CachedQueryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "settings"
        app_label = "core"
