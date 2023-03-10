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


class Socials(CacheInvalidationMixin, idModel, nameModel, statusModel, timeStampModel):
    icon = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255)
    objects = CachedQueryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "socials"
        app_label = "core"
