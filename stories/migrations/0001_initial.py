# Generated by Django 4.0.3 on 2022-07-10 23:01

import ckeditor.fields
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_users_following'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('position', models.IntegerField()),
                ('slug', models.SlugField(null=True, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('authors_note', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('words', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=100)),
                ('released_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('edited_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='editor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'chapters',
            },
        ),
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='stories.categories')),
            ],
            options={
                'verbose_name_plural': 'characters',
            },
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'editors',
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('native_name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'languages',
            },
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'ratings',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'types',
            },
        ),
        migrations.CreateModel(
            name='Universes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.categories')),
            ],
            options={
                'verbose_name_plural': 'universes',
            },
        ),
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('abbreviation', models.CharField(max_length=15, unique=True)),
                ('summary', ckeditor.fields.RichTextField(verbose_name='synopsis')),
                ('cover', models.ImageField(blank=True, max_length=255, null=True, upload_to='')),
                ('released_at', models.DateTimeField()),
                ('featured', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('abandoned', 'Abandoned'), ('complete', 'Complete'), ('haitus', 'Haitus'), ('prerelease', 'Pre-Released'), ('published', 'Published'), ('oneshot', 'One Shot'), ('ongoing', 'Ongoing'), ('draft', 'Draft')], default='draft', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('authors', models.ManyToManyField(blank=True, through='stories.Author', to=settings.AUTH_USER_MODEL)),
                ('characters', models.ManyToManyField(blank=True, related_name='names', to='stories.characters')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='story_dislike', to=settings.AUTH_USER_MODEL)),
                ('editor', models.ManyToManyField(blank=True, related_name='editors', to='stories.editor')),
                ('following', models.ManyToManyField(blank=True, related_name='story_followers', to=settings.AUTH_USER_MODEL)),
                ('genre', models.ManyToManyField(blank=True, to='stories.genres')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.languages')),
                ('likes', models.ManyToManyField(blank=True, related_name='story_likes', to=settings.AUTH_USER_MODEL)),
                ('rating', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='stories.ratings')),
                ('story_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.types')),
                ('tags', models.ManyToManyField(blank=True, to='stories.tag')),
            ],
            options={
                'verbose_name_plural': 'stories',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(default='active', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapter', to='stories.chapters')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='stories.stories')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'bookmarks',
            },
        ),
        migrations.AddField(
            model_name='editor',
            name='story',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='editor_stories', to='stories.stories'),
        ),
        migrations.AddField(
            model_name='editor',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='editor_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='characters',
            name='story',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='story', to='stories.stories'),
        ),
        migrations.AddField(
            model_name='chapters',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.stories'),
        ),
        migrations.AddField(
            model_name='chapters',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categories',
            name='category_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stories.types'),
        ),
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(default='active', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarked', to='stories.stories')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'bookmarks',
            },
        ),
        migrations.AddField(
            model_name='author',
            name='story',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_stories', to='stories.stories'),
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
