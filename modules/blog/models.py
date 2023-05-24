from django.conf import settings
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from versatileimagefield.fields import VersatileImageField


# Create your models here.
class Category(models.Model):
    status_choices = (
        ("Draft", "Draft"),
        ("Published", "Published"),
        ("Unpublished", "Not Published"),
    )
    name = models.CharField(max_length=200, help_text="the category Name")
    slug = models.SlugField(default="name")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=100, choices=status_choices, default="Draft")

    class Meta:
        verbose_name_plural = "Blog Categories"
        app_label = "blog"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:category", kwargs={"category": self.slug})


class Tags(models.Model):
    slug = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag", kwargs={"tag": self.name})

    class Meta:
        verbose_name_plural = "Blog Tags"
        app_label = "blog"


class Topics(models.Model):
    slug = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Blog Topics"
        app_label = "blog"


class Post(models.Model):
    status_choices = (
        ("Draft", "Draft"),
        ("Published", "Published"),
        ("Unpublished", "Not Published"),
    )
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, null=True, blank=True
    )
    # parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, help_text="Don't  have more than one level nested parenting")
    slug = models.CharField(max_length=255, auto_created=True, blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    seo_title = models.CharField(max_length=255, blank=True, null=True)
    seo_description = RichTextField(max_length=255, blank=True, null=True)
    seo_keywords = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=status_choices, default="Draft")
    featured_image = VersatileImageField(max_length=255, blank=True, null=True)
    featured_image_caption = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        verbose_name="Created By",
        on_delete=models.DO_NOTHING,
    )
    meta = models.JSONField(blank=True, null=True)
    tags = models.ManyToManyField(Tags, blank=True, related_name="posts_tags")
    topics = models.ManyToManyField(Topics, related_name="posts_topics", blank=True)
    published_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_parent_path(self, list=None):
        parenturl = []

        if list is not None:
            parenturl = list

        if self.parent is not None:
            parenturl.insert(0, self.parent.slug)
            return self.parent.get_parent_path(parenturl)

        return parenturl

    # display the featured image or a default image
    def get_featured_image(self):
        if self.featured_image:
            return self.featured_image.url
        else:
            return settings.MEDIA_URL + "author-suzy-hazelwood.jpg"

    def get_absolute_url(self):
        # path = ""

        # if self.parent is not None:
        #     parentlisting = self.get_parent_path()
        #     for parent in parentlisting:
        #         # path = path + parent + '/'
        #         if self.parent == parentlisting[-1]:
        #             path = path + parent + "/"
        #         else:
        #             path = path + parent
        #     return reverse("page", kwargs={"path": path, "slug": self.slug})
        # else:
        #     return reverse("page", kwargs={"slug": self.slug})

        # path = path

        # return reverse("page", kwargs={"path": path, "slug": self.slug})
        return reverse(
            "blog:post", kwargs={"category": self.category.slug, "slug": self.slug}
        )

    def get_previous_post(self):
        return (
            Post.objects.filter(published_at__lt=self.published_at)
            .exclude(id=self.id)
            .order_by("-published_at")
            .first()
        )

    def get_next_post(self):
        return (
            Post.objects.filter(published_at__gt=self.published_at)
            .exclude(id=self.id)
            .order_by("published_at")
            .first()
        )

    # get the recommended blog post
    def get_recommended_post(self):
        if self.get_next_post() is not None:
            return self.get_next_post()
        else:
            return self.get_previous_post()

    class Meta:
        verbose_name_plural = "Blog Posts"
        unique_together = (("slug", "user_id"),)
        app_label = "blog"


class Comments(models.Model):
    RATINGS = (
        (1, "1 star"),
        (2, "2 stars"),
        (3, "3 stars"),
        (4, "4 stars"),
        (5, "5 stars"),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reviews")
    parent_review = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="child_reviews",
    )
    content = models.TextField()
    rating = models.IntegerField(choices=RATINGS)
    is_guest = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        app_label = "blog"

    def __str__(self):
        return f"{self.author} - {self.post.title}"

    def get_absolute_url(self):
        return reverse(
            "blog:post",
            kwargs={"category": self.post.category.slug, "slug": self.post.slug},
        )


# class PostViews(models.Model):
#     post_id = models.CharField(max_length=36)
#     ip = models.CharField(max_length=255, blank=True, null=True)
#     agent = models.TextField(blank=True, null=True)
#     referer = models.CharField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)


# class PostVisits(models.Model):
#     post_id = models.CharField(max_length=36)
#     ip = models.CharField(max_length=255, blank=True, null=True)
#     agent = models.TextField(blank=True, null=True)
#     referer = models.CharField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
