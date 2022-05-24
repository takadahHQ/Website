from django.db import models
from django.conf import settings

class Sponsors(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    package_id = models.ForeignKey('Package', on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'sponsors'

class Packages(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    story_id = models.ForeignKey('Stories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    advance = models.IntegerField()
    amount = models.IntegerField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'packages'