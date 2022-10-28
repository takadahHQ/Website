from django.db.models import Q,Count
from django.shortcuts import render, get_object_or_404
from stories.models import Chapter, Stories, Bookmark, Language, Genre, Rating,Type, Universe


def get_stories_by_genre(slug):
    genre = get_genre(slug=slug)
    test = stories = Stories.objects.filter(~Q(status='pending') | ~Q(status='draft'))
    stories = Stories.objects.filter(~Q(status='pending') | ~Q(status='draft'), genre__slug=genre.slug)
    return stories

def get_author_stories_likes(author):
    likes = Stories.objects.filter(author=author).aggregate(total_likes=Count('likes'))['total_likes']
    return likes

def get_stories_by_author(user):
    stories = Stories.objects.filter(~Q(status='pending') | ~Q(status='draft'), author__user__in=[user])
    return stories

def get_total_story_likes(story):
    story = Stories.objects.filter(id=story)
    likes = story.likes_count()
    return likes

def get_total_story_dislikes(story):
    story = Stories.objects.filter(id=story)
    dislikes = story.dislikes_count()
    return dislikes

def get_total_story_follow(story):
    story = Stories.objects.filter(id=story)
    follow = story.following_count()
    return follow