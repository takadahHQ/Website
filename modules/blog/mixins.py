from django.db import models
from django.conf import settings


class statusModel(models.Model):
    status_choices = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )
    status = models.CharField(max_length=100, choices=status_choices, default="active")

    class Meta:
        abstract = True


class timeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class deletedModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class nameModel(models.Model):
    name = models.CharField(max_length=191)

    class Meta:
        abstract = True


class titleModel(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        abstract = True


class userModel(models.Model):
    create_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        related_name="%(class)s_created_by",
        blank=True,
        null=True,
    )
    update_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.DO_NOTHING,
        related_name="%(class)s_updated_by",
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class idModel(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        abstract = True
