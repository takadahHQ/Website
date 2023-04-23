from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.conf import settings


class AdImage(models.Model):
    ad = models.ForeignKey(
        "Ad", on_delete=models.CASCADE, verbose_name="Ad", related_name="images"
    )
    device = models.CharField(
        verbose_name="Device", max_length=2, choices=settings.ADS_DEVICES
    )
    image = VersatileImageField(verbose_name="Image", max_length=255)

    @property
    def size(self):
        size = (
            settings.ADS_ZONES.get(self.ad.zone, {})
            .get("ad_size", {})
            .get(self.device, None)
        )
        return size or settings.ADS_DEFAULT_AD_SIZE

    def __str__(self):
        return self.get_device_display()
