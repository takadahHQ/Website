from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from versatileimagefield.fields import VersatileImageField


class Page(models.Model):
    status_choices = (
        ("Draft", "Draft"),
        ("Published", "Published"),
        ("Unpublished", "Not Published"),
    )
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Don't  have more than one level nested parenting",
    )
    slug = models.CharField(max_length=255, auto_created=True, blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    seo_title = models.CharField(max_length=255, blank=True, null=True)
    seo_description = RichTextField(max_length=255, blank=True, null=True)
    seo_keywords = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=status_choices, default="Draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Pages"
        app_label = "pages"

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

    def get_absolute_url(self):
        path = ""

        if self.parent is not None:
            parentlisting = self.get_parent_path()
            for parent in parentlisting:
                # path = path + parent + '/'
                if self.parent == parentlisting[-1]:
                    path = path + parent + "/"
                else:
                    path = path + parent
            return reverse("page", kwargs={"path": path, "slug": self.slug})
        else:
            return reverse("page", kwargs={"slug": self.slug})

        path = path

        return reverse("page", kwargs={"path": path, "slug": self.slug})
