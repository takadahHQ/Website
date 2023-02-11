from django.urls import reverse
from django.db import models
from modules.stories.models.include import (
    Sluggable,
    idModel,
    nameModel,
    statusModel,
    timeStampModel,
    CachedQueryManager,
    CacheInvalidationMixin,

)


class Language(CacheInvalidationMixin, Sluggable, idModel, nameModel, statusModel, timeStampModel):
    code = models.CharField(max_length=255)
    native_name = models.CharField(max_length=255)
    objects = CachedQueryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "languages"
        app_label = "stories"

    def get_absolute_url(self):
        return reverse("stories:langauage", kwargs={"slug": self.slug})
