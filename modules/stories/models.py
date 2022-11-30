from django.contrib import admin
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import SlugField
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.core.files.images import ImageFile
from . import images as img
from django.core.files import File
from requests import request
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager

from flag.models import Flag

class statusModel(models.Model):
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'), 
        )
    status = models.CharField(max_length=100, choices=status_choices, default='active')

    class Meta:
        abstract = True

class timeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class nameModel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

class idModel(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        abstract = True

class descModel(models.Model):
    description = RichTextField(blank=True, null=True)

    class Meta:
        abstract = True

SLUG_LENGTH = 50


def get_unique_slug(model_instance):
    slugify_title = slugify(model_instance.name, allow_unicode=True)
    if len(slugify_title) > SLUG_LENGTH:
        slug = slugify_title[:SLUG_LENGTH]
    else:
        slug = slugify_title
    slug_copy = slug
    num = 1
    while model_instance.__class__.objects.filter(slug=slug).exists():
        number_attached_slug = '{}-{}'.format(slug_copy, num)

        if len(number_attached_slug) > SLUG_LENGTH:
            trimmed_slug = slug_copy[:-(num + 1)]  # adding 1 because there is hyphen in the slug
            slug = '{}-{}'.format(trimmed_slug, num)
        else:
            slug = number_attached_slug
        num += 1

    return slug


class Sluggable(models.Model):
    slug = models.SlugField(null=True, max_length=30, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
        
class Categories(Sluggable, idModel, nameModel, statusModel, timeStampModel):
    category_type = models.ForeignKey('Type', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Chapter(idModel, statusModel, timeStampModel):
    story = models.ForeignKey('Stories', related_name='chapters', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    edited_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='chapter_editor', on_delete=models.DO_NOTHING)
    position = models.IntegerField()
    slug = models.SlugField(null=True, unique=True)
    title = models.CharField(max_length=255)
    text = RichTextUploadingField()
    authors_note = RichTextField(blank=True, null=True)
    words = models.IntegerField(blank=True, null=True)
    released_at = models.DateTimeField()
    flags = GenericRelation(Flag)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.story.abbreviation + "- chapter-" + f'{self.position}')
            self.words = self.text.count(self.text)
        self.words = self.text.count(self.text)
        super(Chapter, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("story:read", kwargs={"type": self.story.story_type.slug, "story": self.story.slug, "slug": self.slug})

    def get_next(self):
        try:
            next_post = Chapter.objects.get(pk=self.pk).filter(position=self.position + 1)
            return reverse("story:read", kwargs={"type": next_post.story.story_type.slug, "story": next_post.story.slug, "slug": next_post.slug})
        except:
            return None

    def get_previous(self):
        try:
            previous_post = Chapter.objects.get(pk=self.pk).filter(position=self.position - 1)
            return reverse("story:read",kwargs={"type": previous_post.story.story_type.slug, "story": previous_post.story.slug, "slug": previous_post.slug})
        except:
            return None

    def get_reviews(self):
        return self.reviews.filter(parent=None).filter(status='active')

    class Meta:
        verbose_name_plural = 'chapters'


class Review(idModel, statusModel, timeStampModel):
    story = models.ForeignKey('Stories', related_name='reviews', on_delete=models.CASCADE)
    chapter = models.ForeignKey('Chapter', related_name='chapter_reviews', null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent=models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    text = RichTextUploadingField()
    flags = GenericRelation(Flag)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.story.abbreviation + "- chapter-" + f'{self.position}')
    #         self.words = self.text.count(self.text)
    #     self.words = self.text.count(self.text)
    #     super(Chapter, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("story:read", kwargs={"type": self.story.story_type.slug, "story": self.story.slug, "slug": self.slug})

    class Meta:
        verbose_name_plural = 'reviews'
        ordering = ('created_at',)
    
    def __str__(self):
        return self.text[:50]

    def get_reviews(self):
        return Review.objects.filter(parent=self).filter(status='active')

class Bookmark(idModel, statusModel, timeStampModel):
    story = models.ForeignKey('Stories', related_name='bookmarked', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.story.title

    def get_read_position(self):
        story = History.objects.get(story=self.story, user=self.user)
        return story.chapter.position

    def get_read(self):
        story = History.objects.get(story=self.story, user=self.user)
        return story.chapter.get_absolute_url()

    class Meta:
        verbose_name_plural = 'bookmarks'


class History(idModel, statusModel, timeStampModel):
    story = models.ForeignKey('Stories', related_name='history', on_delete=models.CASCADE)
    chapter = models.ForeignKey('Chapter', related_name='chapter', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.story.title

    class Meta:
        verbose_name_plural = 'bookmarks'


class Character(Sluggable, idModel, nameModel, statusModel, timeStampModel):
    story = models.ForeignKey('Stories', related_name='story', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey('Categories', related_name='category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'characters'

class Editor(idModel, statusModel, timeStampModel):
    story = models.ForeignKey('Stories', related_name='editor_stories', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='editor_user', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{} Edited by {}".format(self.story.title, self.user.name())

    class Meta:
        verbose_name_plural = 'editors'


class Author(idModel, statusModel, timeStampModel):
    story = models.ForeignKey('Stories', related_name='author_stories', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='author_user', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{} Written by {}".format(self.story.title, self.user.name())

    class Meta:
        verbose_name_plural = 'authors'



class Genre(Sluggable, descModel, idModel, nameModel, statusModel, timeStampModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'genres'
    
    def get_absolute_url(self):
        return reverse("story:genre", kwargs={"slug": self.slug})

class Language(Sluggable, idModel, nameModel, statusModel, timeStampModel):
    code = models.CharField(max_length=255)
    native_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'languages'
    
    def get_absolute_url(self):
        return reverse("story:langauage", kwargs={"slug": self.slug})


class Rating(Sluggable, idModel, nameModel, descModel, statusModel, timeStampModel):

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'ratings'
    
    def get_absolute_url(self):
        return reverse("story:rating", kwargs={"slug": self.slug})


class Stories(idModel, timeStampModel):
    status_choices = (
        ('abandoned', 'Abandoned'), 
        ('complete', 'Complete'),
        ('haitus', 'Haitus'),
        ('prerelease', 'Pre-Released'),
        ('published', 'Published'),
        ('oneshot', 'One Shot'),
        ('ongoing', 'Ongoing'),
        ('draft', 'Draft'), 
        )
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, unique=True)
    abbreviation = models.CharField(max_length=15, unique=True)
    summary = RichTextField('synopsis')
    cover = models.ImageField(max_length=255, blank=True, null=True)
    story_type = models.ForeignKey('Type', on_delete=models.CASCADE)
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="story_followers", symmetrical=False
    )
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,  blank=True, related_name='story_likes')
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True, related_name='story_dislike')
    author = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Author', related_name='authors', blank=True)
    editor = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Editor', related_name='editors', blank=True)
    language = models.ForeignKey('Language',  on_delete=models.CASCADE)
    genre = models.ManyToManyField('Genre', blank=True)
    characters = models.ManyToManyField('Character', related_name='names', blank=True)
    rating = models.ForeignKey('Rating', on_delete=models.DO_NOTHING, blank=True, null=True)
    released_at = models.DateTimeField()
    featured = models.BooleanField(default=False)
    featured_at = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()
    flags = GenericRelation(Flag)
    status = models.CharField(max_length=100, choices=status_choices, default='draft')

    def __str__(self):
        return self.title

    #@admin.display(description='Following')
    def following_count(self):
        return self.following.count()
    #.display(description='Follower')
    def followers_count(self):
        return self.followers.count()
    # #@admin.display(description='Likes')
    def likes_count(self):
        return self.likes.count()
    # #@admin.display(description='Dislikes')
    def dislikes_count(self):
        return self.dislikes.count()
    # #@admin.display(description='First chapter of Story')
    def get_read_guest(self):
        #hack to get it to work
        if self.chapter_set.first():
            return self.chapter_set.first().get_absolute_url()

    def get_read_user(self, request):
        story = History.objects.filter(user=request.user).get(story=self.story)
        return story.chapter.get_absolute_url()
   
    def create_cover(self):
        name = self.author.first().name()
        file = img.make(name, self.title, self.slug)
        filename = self.slug + '.png'
        self.cover.save(filename, File(file), save=True)
        return self.cover.url


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify('-'.join([self.abbreviation, self.title]))
        # if not self.cover:
        #     self.cover = self.create_cover()

        super(Stories, self).save(*args, **kwargs)

    def get_cover(self):
        if not self.cover:
            self.cover = self.create_cover()
            return self.cover.url
        else:
            return self.cover.url

    def get_absolute_url(self):
        story_type = self.story_type.name
        return reverse("story:show", kwargs={"type": self.story_type.name.lower(), "slug": self.slug})
    
    class Meta:
        verbose_name_plural = 'stories'

class Type(Sluggable,idModel, nameModel, statusModel, timeStampModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'types'
    
    def get_absolute_url(self):
        return reverse("story:type", kwargs={"slug": self.slug})


class Universe(Sluggable, idModel, nameModel, statusModel, timeStampModel):
    category_id = models.ForeignKey('Categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'universes'
