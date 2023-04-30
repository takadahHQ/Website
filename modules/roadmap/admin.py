from django.contrib import admin

from modules.roadmap.models import Feature, Vote, Comment

# Register your models here.
admin.site.register([Feature, Vote, Comment])
