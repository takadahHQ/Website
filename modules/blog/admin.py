from django.contrib import admin
from .models import Category, Post, Tags, Topics


# Register your models here.
class PostInlineTags(admin.TabularInline):
    model = Post.tags.through
    max_num = 5


class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [PostInlineTags]
    search_fields = ["name"]


class PostInlineCategory(admin.StackedInline):
    model = Post
    max_num = 2


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [PostInlineCategory]


class TopicsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "content", "status", "created_at", "updated_at")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                    "category",
                    "user",
                    "featured_image",
                    "featured_image_caption",
                    "content",
                ),
            },
        ),
        (
            "Topics and Tags",
            {
                "classes": ("collapse",),
                "fields": ("tags", "topics"),
            },
        ),
        (
            "SEO",
            {
                "classes": ("collapse",),
                "fields": (
                    "seo_title",
                    "seo_keywords",
                    "seo_description",
                ),
            },
        ),
        (
            "Publish",
            {
                "classes": ("collapse",),
                "fields": ("status", "deleted_at"),
            },
        ),
    )
    prepopulated_fields = {"slug": ("title",)}

    autocomplete_fields = ["tags", "topics"]


# admin.site.register(Category)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(PostViews)
# admin.site.register(PostVisits)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Topics, TopicsAdmin)
admin.site.register(Post, PostAdmin)
