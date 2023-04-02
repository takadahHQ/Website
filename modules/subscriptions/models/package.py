from django.db import models
from modules.subscriptions.models.include import statusModel
from modules.stories.models.stories import Stories
from django.urls import reverse
from django.utils.text import slugify


class Packages(statusModel):
    story = models.ForeignKey(Stories, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, unique=True)
    name = models.CharField(max_length=255)
    advance = models.IntegerField(
        help_text="The amount of Advance chapters the user is entitled to."
    )
    amount = models.IntegerField(help_text="The Amount to charge in USD")

    def __str__(self):
        return "{} ({})".format(self.story.title, self.name)

    class Meta:
        verbose_name = "package"
        verbose_name_plural = "packages"
        app_label = "subscriptions"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify("-".join([self.story.abbreviation, self.name]))
        super(Packages, self).save(*args, **kwargs)

    def get_absolute_url(self):
        story = self.story.pk
        return reverse(
            "sponsor:author:package-update",
            kwargs={"story": story, "pk": self.pk},
        )

    def get_sponsor_link(self):
        story = self.story.id
        return reverse("sponsor:sponsor", kwargs={"story": story, "slug": self.slug})
