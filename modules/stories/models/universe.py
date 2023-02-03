from django.db import models
from modules.stories.models.include import (
    Sluggable,
    idModel,
    nameModel,
    statusModel,
    timeStampModel,
)


class Universe(Sluggable, idModel, nameModel, statusModel, timeStampModel):
    category_id = models.ForeignKey("Categories", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "universes"
        # app_label = "modules.stories"
