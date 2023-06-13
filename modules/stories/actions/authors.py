from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from modules.core.models.users import Users
from modules.stories.actions.user import get_genre
from modules.stories.models import (
    Chapter,
    Stories,
    Bookmark,
    Language,
    Genre,
    Rating,
    Type,
    Universe,
)


def get_stories_by_genre(slug):
    genre = get_genre(slug=slug)
    # test = stories = Stories.objects.filter(~Q(status='pending') | ~Q(status='draft'))
    stories = Stories.objects.filter(
        ~Q(status="pending") | ~Q(status="draft"), genre__slug=genre.slug
    )
    return stories


def get_author_stories_likes(author):
    # queryset = Users.objects.exclude(Q(status="pending") | Q(status="draft"))
    user = get_object_or_404(Users, pk=author.pk)
    likes = user.total_stories_liked_by_other()
    return likes


def get_author_stories_dislikes(author):
    dislikes = Stories.objects.filter(author=author.id).aggregate(
        total_dislikes=Count("dislikes")
    )["total_dislikes"]
    return dislikes


def get_author_stories_followers(author):
    followers = Stories.objects.filter(author=author.id).aggregate(
        total_followers=Count("following")
    )["total_followers"]
    return followers


def get_author_stories_reviews(author):
    reviews = Stories.objects.filter(author=author.id).aggregate(
        total_followers=Count("following")
    )["total_followers"]
    return reviews


def get_author_stories_views(author):
    views = Stories.objects.filter(author=author.id).aggregate(
        total_followers=Count("following")
    )["total_followers"]
    return views


def get_stories_by_author(user):
    stories = Stories.objects.filter(
        ~Q(status="pending") | ~Q(status="draft"), author=user.id
    )
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


def get_daily_earnings(author):
    earned = author.id
    return earned


def get_weekly_earnings(author):
    earned = author.id
    return earned


def get_monthly_earnings(author):
    earned = author.id
    return earned


def get_chapter(story: any, chapter: any, user: any = None):
    chapter = Chapter.objects.get(story__slug=story, slug=chapter)

    if chapter.is_last():
        chapter.prefetch_related(
            "story__packages",
        )
    previous_chapter, next_chapter = chapter.get_previous_and_next_chapters(user=user)
    return chapter  # , previous_chapter, next_chapter
