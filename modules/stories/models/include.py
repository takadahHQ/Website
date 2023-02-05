from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class statusModel(models.Model):
    status_choices = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )
    status = models.CharField(max_length=100, choices=status_choices, default="active")

    class Meta:
        abstract = True
        app_label = "stories"


class timeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class nameModel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class idModel(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        abstract = True


class descModel(models.Model):
    description = RichTextField(blank=True, null=True)

    class Meta:
        abstract = True


SLUG_LENGTH = 50


def get_unique_slug(model_instance):
    slugify_title = slugify(model_instance.name, allow_unicode=True)
    if len(slugify_title) > SLUG_LENGTH:
        slug = slugify_title[:SLUG_LENGTH]
    else:
        slug = slugify_title
    slug_copy = slug
    num = 1
    while model_instance.__class__.objects.filter(slug=slug).exists():
        number_attached_slug = "{}-{}".format(slug_copy, num)

        if len(number_attached_slug) > SLUG_LENGTH:
            trimmed_slug = slug_copy[
                : -(num + 1)
            ]  # adding 1 because there is hyphen in the slug
            slug = "{}-{}".format(trimmed_slug, num)
        else:
            slug = number_attached_slug
        num += 1

    return slug


class Sluggable(models.Model):
    slug = models.SlugField(null=True, max_length=30, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug