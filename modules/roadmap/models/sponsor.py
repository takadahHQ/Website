from django.db import models
from modules.subscriptions.models.include import statusModel
import datetime


def expire():
    return datetime.datetime.today() + datetime.timedelta(days=30)


class Sponsors(statusModel):
    package = models.ForeignKey("Packages", on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    expire_at = models.DateField(default=expire(), editable=False)

    class Meta:
        verbose_name = "sponsor"
        verbose_name_plural = "sponsors"
        app_label = "subscriptions"
