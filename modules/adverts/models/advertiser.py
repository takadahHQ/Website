from django.db import models
from modules.adverts.models.include import statusModel
from django.urls import reverse


class Advertiser(statusModel):
    """A Model for our Advertiser."""

    company_name = models.CharField(verbose_name="Company Name", max_length=255)
    website = models.URLField(verbose_name="Company Site")

    class Meta:
        verbose_name = "Advertiser"
        verbose_name_plural = "Advertisers"
        app_label = "adverts"
        ordering = ("company_name",)

    def __str__(self):
        return self.company_name

    def get_website_url(self):
        return self.website

    # def get_absolute_url(self):
    #     story = self.story.pk
    #     return reverse(
    #         "sponsor:author:package-update",
    #         kwargs={"story": story, "pk": self.pk},
    #     )
