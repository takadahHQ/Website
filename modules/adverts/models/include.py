from django.db import models
from django.conf import settings
from django.db.models import QuerySet
from django.utils import timezone
from django.db.models import Manager, Count
import random


class AdQuerySet(QuerySet):
    def public(self):
        return self.filter(
            publication_date__lte=timezone.now(),
            publication_date_end__gt=timezone.now(),
        )

    def zone_ads(self, zone):
        return self.filter(zone=zone)


class statusModel(models.Model):
    status_choices = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        verbose_name="Created By",
        on_delete=models.DO_NOTHING,
    )
    status = models.CharField(max_length=100, choices=status_choices, default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AdManager(Manager):
    def get_queryset(self):
        return AdQuerySet(self.model)

    def public(self):
        return self.get_queryset().public()

    def zone_ads(self, zone):
        return self.get_queryset().zone_ads(zone)

    def random_ad(self, zone):
        ads = []
        for ad in self.zone_ads(zone).public():
            ads += [ad] * ad.weight
        if not ads:
            return None
        return random.choice(ads)
