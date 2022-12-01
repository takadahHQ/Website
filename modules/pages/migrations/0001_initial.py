# Generated by Django 4.0.3 on 2022-07-22 16:41

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Page",
            fields=[
                (
                    "slug",
                    models.CharField(
                        auto_created=True, blank=True, max_length=255, null=True
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255, null=True)),
                (
                    "content",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True
                    ),
                ),
                ("seo_title", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "seo_description",
                    ckeditor.fields.RichTextField(
                        blank=True, max_length=255, null=True
                    ),
                ),
                ("seo_keywords", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Draft", "Draft"),
                            ("Published", "Published"),
                            ("Unpublished", "Not Published"),
                        ],
                        default="Draft",
                        max_length=100,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        help_text="Don't  have more than one level nested parenting",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pages.page",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Pages",
            },
        ),
    ]
