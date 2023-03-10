from django.db import models
from django.conf import settings
from modules.core.models.include import (
    idModel,
    nameModel,
    timeStampModel,
    CacheInvalidationMixin,
    CachedQueryManager,
)


class Wallets(CacheInvalidationMixin, idModel, nameModel, timeStampModel):
    holder_type = models.CharField(max_length=255)
    holder_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)
    uuid = models.CharField(unique=True, max_length=36)
    description = models.CharField(max_length=255, blank=True, null=True)
    meta = models.JSONField(blank=True, null=True)
    balance = models.DecimalField(max_digits=64, decimal_places=0)
    decimal_places = models.PositiveSmallIntegerField()

    objects = CachedQueryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "wallets"
        unique_together = (("holder_type", "holder_id", "slug"),)
        app_label = "core"
