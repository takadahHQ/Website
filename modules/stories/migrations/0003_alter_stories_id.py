# Generated by Django 4.1.7 on 2023-03-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stories", "0002_alter_stories_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stories",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
