from django.db import models
from modules.subscriptions.models.include import statusModel
from modules.stories.models.stories import Stories
from django.urls import reverse


class Packages(statusModel):
    story = models.ForeignKey(Stories, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    advance = models.IntegerField(
        help_text="The amount of Advance chapters the user is entitled to."
    )
    amount = models.IntegerField(help_text="The Amount to charge in USD")

    def __str__(self):
        return self.story.title + self.name

    class Meta:
        verbose_name = "package"
        verbose_name_plural = "packages"
        app_label = "subscriptions"

    def get_absolute_url(self):
        story = self.story.pk
        return reverse(
            "sponsor:author:package-update",
            kwargs={"story": story, "pk": self.pk},
        )
