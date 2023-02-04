from django.urls import reverse
from modules.stories.models.include import (
    Sluggable,
    idModel,
    nameModel,
    statusModel,
    timeStampModel,
    descModel,
)


class Rating(Sluggable, idModel, nameModel, descModel, statusModel, timeStampModel):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "ratings"
        app_label = "stories"

    def get_absolute_url(self):
        return reverse("stories:rating", kwargs={"slug": self.slug})
