from django.urls import reverse
from modules.stories.models.include import (
    Sluggable,
    idModel,
    nameModel,
    statusModel,
    timeStampModel,
    descModel,
    CacheInvalidationMixin,
    CachedQueryManager,
)


class Genre(CacheInvalidationMixin ,Sluggable, descModel, idModel, nameModel, statusModel, timeStampModel):
    objects = CachedQueryManager()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "genres"
        # app_label = "modules_stories"

    def get_absolute_url(self):
        return reverse("stories:genre", kwargs={"slug": self.slug})
