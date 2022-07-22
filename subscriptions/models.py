from django.db import models
from django.conf import settings
import datetime

# Create your models here.
def expire():
    return datetime.datetime.today() + datetime.timedelta(days=15)

class Sponsors(models.Model):
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'), 
        )
    # id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    package = models.ForeignKey('Package', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_date = models.DateField(auto_now_add = True)
    expire_at = models.DateField(default=expire, editable=False)
    status = models.CharField(choices=status_choices, default='active')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'sponsors'

class Packages(models.Model):
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'), 
        )
    # id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    story = models.ForeignKey('Stories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    advance = models.IntegerField()
    amount = models.IntegerField()
    status = models.CharField(choices=status_choices, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'packages'