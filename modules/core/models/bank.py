from django.db import models
from django.conf import settings
from modules.core.models.include import (
    idModel,
    statusModel,
    nameModel,
    timeStampModel,
    CacheInvalidationMixin,
    CachedQueryManager,
)


class Bank(CacheInvalidationMixin, idModel, nameModel, statusModel, timeStampModel):
    holder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    holder_name = models.CharField(max_length=255)
    swift = models.CharField(max_length=255)
    iban = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    account_number = models.CharField(max_length=32)

    objects = CachedQueryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "banks"
        app_label = "core"
