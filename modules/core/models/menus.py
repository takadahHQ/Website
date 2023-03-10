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


class Menus(CacheInvalidationMixin, idModel, nameModel, statusModel, timeStampModel):
    position_choices = (
        ("header", "Header"),
        ("footer", "Footer"),
    )

    position = models.CharField(
        max_length=100, choices=position_choices, default="header"
    )
    parent_id = models.ForeignKey(
        "Menus", on_delete=models.CASCADE, blank=True, null=True
    )
    image = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255)
    objects = CachedQueryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "menus"
        app_label = "core"
