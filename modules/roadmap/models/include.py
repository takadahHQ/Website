from django.db import models
from django.conf import settings


class statusModel(models.Model):
    status_choices = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=status_choices, default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
