# Generated by Django 4.1.7 on 2023-04-23 07:52

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_translator_stories_translator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='cover',
            field=versatileimagefield.fields.VersatileImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]
