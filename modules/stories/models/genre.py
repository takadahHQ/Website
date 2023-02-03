from django.urls import reverse
from modules.stories.models.include import (
    Sluggable,
    idModel,
    nameModel,
    statusModel,
    timeStampModel,
    descModel,
)


class Genre(Sluggable, descModel, idModel, nameModel, statusModel, timeStampModel):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "genres"
        # app_label = "modules_stories"

    def get_absolute_url(self):
        return reverse("stories:genre", kwargs={"slug": self.slug})
