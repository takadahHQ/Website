from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from flag.models import Flag
from modules.stories.models.include import (
    idModel,
    statusModel,
    timeStampModel,
)


class Review(idModel, statusModel, timeStampModel):
    story = models.ForeignKey(
        "Stories", related_name="reviews", on_delete=models.CASCADE
    )
    chapter = models.ForeignKey(
        "Chapter",
        related_name="chapter_reviews",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    text = RichTextUploadingField()
    flags = GenericRelation(Flag)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.story.abbreviation + "- chapter-" + f'{self.position}')
    #         self.words = self.text.count(self.text)
    #     self.words = self.text.count(self.text)
    #     super(Chapter, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("stories:read", kwargs={"type": self.story.story_type.slug, "story": self.story.slug, "slug": self.slug})

    class Meta:
        verbose_name_plural = "reviews"
        ordering = ("created_at",)

    def __str__(self):
        return self.text[:50]

    def get_reviews(self):
        return Review.objects.filter(parent=self).filter(status="active")
