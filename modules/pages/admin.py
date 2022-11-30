from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent', 'content', 'status', 'created_at', 'updated_at')
    fields = ('title', 'slug', 'parent', 'content', 'status','seo_title', 'seo_keywords', 'seo_description')
    prepopulated_fields = {"slug": ("title",)}
    # search('title', 'slug')
admin.site.register(Page, PageAdmin)