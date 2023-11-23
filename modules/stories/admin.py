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

    def change_view(self, request, object_id, form_url="", extra_context=None):
        story = self.get_object(request, object_id)
        extra_context = extra_context or {}

        # Get the story analytics
        story_analytics = story.get_story_analytics()
        service = story.service.first()
        if service:
            daily_stats = service.get_daily_stats()

        # Include the story analytics in the extra_context
        extra_context["story_analytics"] = story_analytics
        if daily_stats:
            extra_context["daily_stats"] = daily_stats

        return super().change_view(
            request, object_id, form_url, extra_context=extra_context
        )

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


class ChapterAdmin(admin.ModelAdmin):
    list_display = ("title", "story", "released_at", "words")
    # Add other fields you want to display in the list view

    def change_view(self, request, object_id, form_url="", extra_context=None):
        chapter = self.get_object(request, object_id)
        extra_context = extra_context or {}

        # Get the chapter analytics
        chapter_analytics = chapter.get_chapter_analytics()

        # Include the chapter analytics in the extra_context
        extra_context["chapter_analytics"] = chapter_analytics

        return super().change_view(
            request, object_id, form_url, extra_context=extra_context
        )


# admin.site.register(Tag)
admin.site.register(Type, MainAdmin)
admin.site.register(Categories)
admin.site.register(Genre, MainAdmin)
admin.site.register(Language, MainAdmin)
admin.site.register(Rating, MainAdmin)
admin.site.register(Bookmark)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Character)
admin.site.register(Universe)
admin.site.register(Author)
admin.site.register(Stories, StoriesAdmin)
admin.site.register(Review)
