from django.db import models
from django.conf import settings
from modules.core.models.include import (
    idModel,
    timeStampModel,
    CacheInvalidationMixin,
    CachedQueryManager,
)
from modules.core.models.transactions import Transactions


class Transfers(CacheInvalidationMixin, idModel, timeStampModel):
    status_choices = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )

    from_type = models.CharField(max_length=255)
    from_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="sender", on_delete=models.CASCADE
    )
    to_type = models.CharField(max_length=255)
    to_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="reciever", on_delete=models.CASCADE
    )
    status = models.CharField(max_length=100, choices=status_choices, default="active")
    status_last = models.CharField(max_length=8, blank=True, null=True)
    deposit = models.ForeignKey(
        Transactions, related_name="deposits", on_delete=models.DO_NOTHING
    )
    withdraw = models.ForeignKey(
        Transactions, related_name="withdrawals", on_delete=models.DO_NOTHING
    )
    discount = models.DecimalField(max_digits=64, decimal_places=0)
    fee = models.DecimalField(max_digits=64, decimal_places=0)
    uuid = models.CharField(unique=True, max_length=36)

    objects = CachedQueryManager()

    def __str__(self):
        return self.fee

    class Meta:
        verbose_name_plural = "transfers"
        app_label = "core"
