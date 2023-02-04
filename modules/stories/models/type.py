from django.urls import reverse
from modules.stories.models.include import (
    Sluggable,
    idModel,
    nameModel,
    statusModel,
    timeStampModel,
)


class Type(Sluggable, idModel, nameModel, statusModel, timeStampModel):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "types"
        app_label = "stories"

    def get_absolute_url(self):
        return reverse("stories:type", kwargs={"slug": self.slug})
