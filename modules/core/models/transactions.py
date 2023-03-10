from django.db import models
from django.conf import settings
from modules.core.models.include import (
    idModel,
    timeStampModel,
    CacheInvalidationMixin,
    CachedQueryManager,
)


class Transactions(CacheInvalidationMixin, idModel, timeStampModel):
    payable_type = models.CharField(max_length=255)
    payable_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wallet = models.ForeignKey("Wallets", models.DO_NOTHING)
    trans_type = models.CharField(max_length=8)
    amount = models.DecimalField(max_digits=64, decimal_places=0)
    confirmed = models.IntegerField()
    meta = models.JSONField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=36)
    objects = CachedQueryManager()

    def __str__(self):
        return self.amount

    class Meta:
        verbose_name_plural = "transactions"
        app_label = "core"
