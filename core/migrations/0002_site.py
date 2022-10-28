# Generated by Django 4.0.3 on 2022-09-11 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('hero_header', models.CharField(max_length=255)),
                ('hero_text', models.CharField(max_length=255)),
                ('newsletter_header', models.CharField(max_length=255)),
                ('newsletter_text', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'site',
            },
        ),
    ]