# Generated by Django 3.1.1 on 2020-09-15 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('state', models.SmallIntegerField(choices=[(1, 'Unflagged'), (2, 'Flagged'), (3, 'Flag rejected by the moderator'), (5, 'Content modified by the author'), (4, 'Creator notified')], default=1)),
                ('count', models.PositiveIntegerField(default=0)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flags_against', to=settings.AUTH_USER_MODEL)),
                ('moderator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flags_moderated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Flag',
                'unique_together': {('content_type', 'object_id')},
            },
        ),
        migrations.CreateModel(
            name='FlagInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_flagged', models.DateTimeField(auto_now_add=True)),
                ('reason', models.SmallIntegerField(choices=[(1, 'Spam | Exists only to promote a service '), (2, 'Abusive | Intended at promoting hatred'), (100, 'Something else')], default=1)),
                ('info', models.TextField(blank=True, null=True)),
                ('flag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flags', to='flag.flag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flags_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Flag Instance',
                'verbose_name_plural': 'Flag Instances',
                'ordering': ['-date_flagged'],
                'unique_together': {('flag', 'user')},
            },
        ),
    ]
