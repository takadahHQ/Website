from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from modules.core.models.include import (
    idModel,
    statusModel,
    timeStampModel,
    CacheInvalidationMixin,
    CachedQueryManager,
)
from versatileimagefield.fields import VersatileImageField


class Kycs(CacheInvalidationMixin, idModel, statusModel, timeStampModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    middle_name = models.CharField(max_length=70, blank=True, null=True)
    country_id = models.PositiveIntegerField()
    document_type = models.CharField(max_length=15)
    selfie = VersatileImageField(blank=True, null=True)
    rejected_reason = RichTextField(blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    rejected_at = models.DateTimeField(blank=True, null=True)

    objects = CachedQueryManager()

    class Meta:
        verbose_name_plural = "kycs"
        app_label = "core"

    def __str__(self):
        return self.first_name
