from django.db import models
from modules.adverts.models.include import statusModel


class Category(statusModel):
    """a Model to hold the different Categories for adverts"""

    title = models.CharField(verbose_name="Title", max_length=255)
    description = models.TextField(verbose_name="Description", blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("title",)

    def __str__(self):
        return self.title
