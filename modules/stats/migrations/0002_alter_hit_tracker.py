# Generated by Django 4.1.7 on 2023-06-07 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hit',
            name='tracker',
            field=models.TextField(choices=[('BACK', 'Backend'), ('PIXEL', 'Image'), ('JS', 'JavaScript'), ('API', 'Api (noscript)')]),
        ),
    ]