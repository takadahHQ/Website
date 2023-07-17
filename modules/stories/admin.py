from django.contrib import admin
from .models import (
    Stories,
    Categories,
    Chapter,
    Character,
    Bookmark,
    Genre,
    Language,
    Rating,
    Universe,
    Type,
    Author,
    Editor,
    Review,
    Translator,
)

from import_export import resources

# Register your models here.


class StoriesResource(resources.ModelResource):
    class Meta:
        model = Stories


class EditorInline(admin.StackedInline):
    model = Editor
    max_num = 3


class AuthorInline(admin.StackedInline):
    model = Author
    max_num = 3


class TranslatorInline(admin.StackedInline):
    model = Translator
    max_num = 3


class ReviewInline(admin.StackedInline):
    model = Review
    max_num = 5


class StoriesAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "cover",
        "summary",
        "status",
        "released_at",
        "created_at",
        "updated_at",
    )
    inlines = [AuthorInline, TranslatorInline, EditorInline, ReviewInline]
    prepopulated_fields = {
        "slug": (
            "abbreviation",
            "title",
        )
    }
    resource_class = StoriesResource

    # fieldsets = (
    #     (None, {
    #         "fields": ('title', 'slug', 'category','featured_image', 'featured_image_caption', 'content',),
    #     }),
    #     ('Topics and Tags',{
    #         'classes': ('collapse',),
    #         'fields': ('tags', 'topics'),
    #     }),
    #     ('SEO', {
    #         'classes': ('collapse',),
    #         'fields': ('seo_title', 'seo_keywords', 'seo_description',)
    #     }),
    #     ('Publish', {
    #         'classes': ('collapse',),
    #         'fields': ('status', 'published_at', 'deleted_at')
    #     })
    # )
    # prepopulated_fields = {"slug": ("title",)}

    # autocomplete_fields = ['tags', 'title']


class MainAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("name",)}


# admin.site.register(Tag)
admin.site.register(Type, MainAdmin)
admin.site.register(Categories)
admin.site.register(Genre, MainAdmin)
admin.site.register(Language, MainAdmin)
admin.site.register(Rating, MainAdmin)
admin.site.register(Bookmark)
admin.site.register(Chapter)
admin.site.register(Character)
admin.site.register(
    Universe,
)
admin.site.register(Author)
admin.site.register(Stories, StoriesAdmin)
admin.site.register(Review)
