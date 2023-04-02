# Generated by Django 4.1.7 on 2023-03-23 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0006_alter_sponsors_expire_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="sponsors",
            name="reference",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="sponsors",
            name="expire_at",
            field=models.DateField(
                default=datetime.datetime(2023, 4, 22, 15, 33, 11, 989600),
                editable=False,
            ),
        ),
    ]