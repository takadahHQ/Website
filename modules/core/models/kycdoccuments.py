from django.db import models
from modules.core.models.include import (
    idModel,
    nameModel,
    statusModel,
    timeStampModel,
    CacheInvalidationMixin,
    CachedQueryManager,
)


class KycDocuments(
    CacheInvalidationMixin, idModel, nameModel, statusModel, timeStampModel
):
    kyc = models.ForeignKey("Kycs", on_delete=models.CASCADE)
    path = models.CharField(max_length=255, blank=True, null=True)
    objects = CachedQueryManager()

    def __str__(self):
        return self.kyc.first_name + " " + self.name

    class Meta:
        verbose_name_plural = "kyc_documents"
        app_label = "core"
