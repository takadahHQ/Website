# Generated by Django 4.1.2 on 2023-02-13 16:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("stories", "0002_alter_stories_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="Packages",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=100,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "advance",
                    models.IntegerField(
                        help_text="The amount of Advance chapters the user is entitled to."
                    ),
                ),
                (
                    "amount",
                    models.IntegerField(help_text="The Amount to charge in USD"),
                ),
                (
                    "story",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stories.stories",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "package",
                "verbose_name_plural": "packages",
            },
        ),
        migrations.CreateModel(
            name="Sponsors",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=100,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("payment_date", models.DateField(auto_now_add=True)),
                (
                    "expire_at",
                    models.DateField(
                        default=datetime.datetime(2023, 3, 15, 20, 4, 15, 854776),
                        editable=False,
                    ),
                ),
                (
                    "package",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="subscriptions.packages",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "sponsor",
                "verbose_name_plural": "sponsors",
            },
        ),
    ]