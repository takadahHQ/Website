# Generated by Django 4.0.3 on 2022-08-21 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_users_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='status',
            new_name='gender',
        ),
    ]
