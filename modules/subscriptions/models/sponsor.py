from django.db import models
from modules.subscriptions.models.include import statusModel
import datetime
from django.urls import reverse


def expire():
    return datetime.datetime.today() + datetime.timedelta(days=30)


class Sponsors(statusModel):
    package = models.ForeignKey(
        "Packages", related_name="sponsor", on_delete=models.CASCADE
    )
    payment_date = models.DateField(auto_now_add=True)
    expire_at = models.DateField()
    reference = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.reference

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if the instance is being created (not updated)
            self.expire_at = datetime.datetime.today() + datetime.timedelta(days=30)

    class Meta:
        verbose_name = "sponsor"
        verbose_name_plural = "sponsors"
        app_label = "subscriptions"

    def get_absolute_url(self):
        story = self.package.story.pk
        return reverse(
            "sponsor:sponsor-update",
            kwargs={"story": story, "pk": self.pk},
        )
