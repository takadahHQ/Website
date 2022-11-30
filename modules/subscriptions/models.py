from django.db import models
from django.conf import settings
import datetime




class statusModel(models.Model):
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'), 
        )
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=status_choices, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
def expire():
    return datetime.datetime.today() + datetime.timedelta(days=15)

class Sponsors(statusModel):
    package = models.ForeignKey('Package', on_delete=models.CASCADE) 
    payment_date = models.DateField(auto_now_add = True)
    expire_at = models.DateField(default=expire(), editable=False)

    class Meta:
        verbose_name_plural = 'sponsors'

class Packages(statusModel):
    story = models.ForeignKey('Stories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    advance = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        verbose_name_plural = 'packages'