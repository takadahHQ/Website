from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.conf import settings
from modules.adverts.models.include import statusModel


class AdMedia(statusModel):
    ad = models.ForeignKey(
        "Ad", on_delete=models.CASCADE, verbose_name="Ad", related_name="media"
    )
    device = models.CharField(
        verbose_name="Device", max_length=2, choices=settings.ADS_DEVICES
    )
    image = VersatileImageField(verbose_name="Image", max_length=255)
    media = models.FileField(
        verbose_name="Media",
        null=True,
        blank=True,
        max_length=255,
        help_text="Please only Upload webm or mp4 for video files<br> And mp3 or wav for audio files",
    )
    is_audio = models.BooleanField(default=False)
    is_media = models.BooleanField(default=False)

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

    def save(self, *args, **kwargs):
        if self.media.name.endswith(".webm") or self.media.name.endswith(".mp4"):
            self.is_audio = False
            self.is_media = True
        elif self.media.name.endswith(".mp3") or self.media.name.endswith(".wav"):
            self.is_audio = True
            self.is_media = True
        else:
            raise ValueError("Invalid file type")
        super().save(*args, **kwargs)
