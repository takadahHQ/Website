# Generated by Django 4.1.2 on 2023-02-17 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sponsors",
            name="expire_at",
            field=models.DateField(
                default=datetime.datetime(2023, 3, 19, 14, 29, 55, 336944),
                editable=False,
            ),
        ),
    ]