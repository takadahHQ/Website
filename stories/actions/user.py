from django.db.models import Q,Count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from taggit.models import Tag
from stories.models import Chapter, Stories, Bookmark, Language, Genre, Rating,Type, Universe

def get_genre(slug):
    queryset = Genre.objects.exclude(Q(status='pending') | Q(status='draft'))
    genre = get_object_or_404(queryset, slug=slug)
    return genre

def get_stories_by_genre(slug):
    genre = get_genre(slug=slug)
    test = stories = Stories.objects.filter(~Q(status='pending') | ~Q(status='draft'))
    stories = Stories.objects.filter(~Q(status='pending') | ~Q(status='draft'), genre__slug=genre.slug)
    return stories

def get_tag(slug):
    tag = get_object_or_404(Tag, slug=slug)
    return tag

def get_stories_by_tag(slug):
    tag = get_tag(slug=slug)
    stories = Stories.objects.filter(~Q(status='pending') | ~Q(status='draft'), tags__slug__in=[tag.slug])
    return stories

def get_type(slug):
    types = get_object_or_404(Type, slug=slug)
    return types

def get_stories_by_type(slug):
    types = get_type(slug=slug)
    stories = Stories.objects.filter(~Q(status='pending') | ~Q(status='draft'), story_type__slug__in=[types.slug])
    return stories

def get_language(slug):
    language = Language.objects.filter(~Q(status='pending') | ~Q(status='draft'), language__slug=slug)
    return language

def get_story(slug):
    story = Stories.objects.select_related('story_type', 'language','rating').filter(~Q(status='pending') | ~Q(status='draft'), slug=slug).annotate(chapter_count=Count('chapter'))
    return story

def get_all_ratings(slug):
    ratings = Rating.objects.filter(~Q(status='pending') | ~Q(status='draft'), rating__slug=self.kwargs.get('slug'))
    return ratings

def like_story(user, slug):
    story = get_object_or_404(Stories, id=slug)
    if story.likes.filter(id=user.id).exists():
        story.likes.remove(user)
        story.save()
    else:
        story.likes.add(user)
        story.save()
    return story

def dislike_story(user, slug):
    story = get_object_or_404(Stories, id=slug)
    if story.dislikes.filter(id=user.id).exists():
        story.dislikes.remove(user)
        story.save()
    else:
        story.dislikes.add(user)
        story.save()
    return story

def follow_story(user, slug):
    story = get_object_or_404(Stories, id=slug)
    if story.following.filter(id=user.id).exists():
        story.following.remove(user)
        story.save()
    else:
        story.following.add(user)
        story.save()
    return story

def bookmark_story(user, slug):
    story = get_object_or_404(Stories, id=slug)
    bookmark = Bookmark.objects.update_or_create(story=story, user=user, defaults={'story': story, 'user':user,})
    bookmark.save()
    bookmarks = Bookmark.objects.get(story=story.id)
    return bookmarks
    