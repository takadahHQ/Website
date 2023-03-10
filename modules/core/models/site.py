from django.db import models
from django.conf import settings
from modules.core.models.include import (
    idModel,
    nameModel,
    timeStampModel,
    CacheInvalidationMixin,
    CachedQueryManager,
)


class Site(CacheInvalidationMixin, idModel, nameModel, timeStampModel):
    hero_header = models.CharField(max_length=255)
    hero_text = models.CharField(max_length=255)
    newsletter_header = models.CharField(max_length=255)
    newsletter_text = models.CharField(max_length=255)

    objects = CachedQueryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "site"
        app_label = "core"
