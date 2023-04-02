# Generated by Django 4.1.7 on 2023-03-23 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0007_sponsors_reference_alter_sponsors_expire_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="packages",
            name="slug",
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="sponsors",
            name="expire_at",
            field=models.DateField(
                default=datetime.datetime(2023, 4, 22, 15, 50, 11, 493016),
                editable=False,
            ),
        ),
    ]