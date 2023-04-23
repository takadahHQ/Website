from django.db import models


class Click(models.Model):
    """
    The AdClick model will record every click that a add gets
    """

    ad = models.ForeignKey(
        "Ad", on_delete=models.CASCADE, verbose_name="Ad", related_name="clicks"
    )
    click_date = models.DateTimeField(verbose_name="When", auto_now_add=True)
    source_ip = models.GenericIPAddressField(
        verbose_name="Source IP Address", null=True, blank=True
    )
    session_id = models.CharField(
        verbose_name="Source Session ID", max_length=40, null=True, blank=True
    )

    class Meta:
        verbose_name = "Ad Click"
        verbose_name_plural = "Ad Clicks"
        index_together = (
            "ad",
            "session_id",
        )

    def __str__(self):
        # return force_text(self.ad.title)
        return self.ad.title
