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
    expire_at = models.DateField(default=expire(), editable=False)

    def __str__(self):
        return self.name

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
