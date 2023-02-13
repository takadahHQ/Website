from django.db.models import Q, Count, Prefetch
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from taggit.models import Tag
from django.contrib.auth import get_user_model
from modules.stories.models import (
    Chapter,
    Stories,
    Bookmark,
    Language,
    Genre,
    Rating,
    Type,
    History,
    Universe,
)
from modules.core.models import Users
from modules.subscriptions.models import Sponsors, Packages
from modules.stories.models.review import Review
import pandas as pd

try:
    mindsdb = __import__("mindsdb")
except ImportError:
    mindsdb = None


def get_genre(slug):
    queryset = Genre.objects.exclude(Q(status="pending") | Q(status="draft"))
    genre = get_object_or_404(queryset, slug=slug)
    return genre


# def get_user(slug):
#     queryset = Users.objects.exclude(Q(status='pending') | Q(status='draft'))
#     genre = get_object_or_404(queryset, slug=slug)
#     return genre


def get_stories_by_genre(slug):
    genre = get_genre(slug=slug)
    test = stories = Stories.objects.filter(~Q(status="pending") | ~Q(status="draft"))
    stories = Stories.objects.filter(
        ~Q(status="pending") | ~Q(status="draft"), genre__slug=genre.slug
    ).prefetch_related(
        "story_type",
        "language",
        "rating",
        "flags",
        "following",
        "likes",
        "dislikes",
        "author",
        "editor",
        "genre",
        "characters",
        "tags",
    )
    return stories


def get_tag(slug):
    tag = get_object_or_404(Tag, slug=slug)
    return tag


def get_stories_by_tag(slug):
    tag = get_tag(slug=slug)
    stories = Stories.objects.filter(
        ~Q(status="pending") | ~Q(status="draft"), tags__slug__in=[tag.slug]
    ).prefetch_related(
        "story_type",
        "language",
        "rating",
        "flags",
        "following",
        "likes",
        "dislikes",
        "author",
        "editor",
        "genre",
        "characters",
        "tags",
    )
    return stories


def get_type(slug):
    types = get_object_or_404(Type, slug=slug)
    return types


def get_stories_by_type(slug):
    types = get_type(slug=slug)
    stories = Stories.objects.filter(
        ~Q(status="pending") | ~Q(status="draft"), story_type__slug__in=[types.slug]
    ).prefetch_related(
        "story_type",
        "language",
        "rating",
        "flags",
        "following",
        "likes",
        "dislikes",
        "author",
        "editor",
        "genre",
        "characters",
        "tags",
    )
    return stories


def get_stories_by_author(user):
    # types = get_type(slug=slug)
    stories = Stories.objects.filter(
        ~Q(status="pending") | ~Q(status="draft"), author=user.id
    ).prefetch_related(
        "story_type",
        "language",
        "rating",
        "flags",
        "following",
        "likes",
        "dislikes",
        "author",
        "editor",
        "genre",
        "characters",
        "tags",
    )
    return stories


def get_language(slug):
    language = Language.objects.filter(
        ~Q(status="pending") | ~Q(status="draft"), language__slug=slug
    )
    return language


def get_story(slug: str, type: str):
    story = (
        Stories.objects.filter(~Q(status="pending") | ~Q(status="draft"))
        .filter(story_type__slug=type)
        .annotate(chapters_count=Count("chapters"))
        .prefetch_related(
            "story_type",
            "language",
            "rating",
            "following",
            "likes",
            "dislikes",
            "author",
            "editor",
            "genre",
            "characters",
            "tags",
            Prefetch(
                "reviews",
                queryset=Review.objects.filter(parent=None).filter(status="active"),
            ),
            "story__chapters",
            "chapters",
        )
        .get(slug=slug)
    )
    return story


def get_all_ratings(slug):
    ratings = Rating.objects.filter(
        ~Q(status="pending") | ~Q(status="draft"), rating__slug=slug
    )
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
    bookmark = Bookmark.objects.update_or_create(
        story=story,
        user=user,
        defaults={
            "story": story,
            "user": user,
        },
    )
    bookmark.save()
    bookmarks = Bookmark.objects.get(story=story.id)
    return bookmarks


def get_bookmarked_stories(user):
    bookmarks = (
        Bookmark.objects.filter(user=user)
        .filter(status="active")
        .order_by("-created_at")
        .prefetch_related("story")
    )
    return bookmarks


def get_user_histories(user):
    histories = (
        History.objects.filter(user=user)
        .filter(status="active")
        .order_by("-created_at")
        .prefetch_related(
            "story",
            "chapter",
            "story__story_type",
        )
    )
    return histories


def get_featured_stories(count):
    stories = (
        Stories.objects.filter(featured=True)
        .select_related("story_type", "language", "rating", "flags")
        .filter(status="active")
        .prefetch_related(
            "story_type",
            "language",
            "rating",
            "flags",
            "following",
            "likes",
            "dislikes",
            "author",
            "editor",
            "genre",
            "characters",
            "tags",
        )[:count]
    )
    return stories


def get_weekly_stories(count):
    stories = (
        Stories.objects.filter(featured=True)
        .filter(status="active")
        .prefetch_related(
            "story_type",
            "language",
            "rating",
            "flags",
            "following",
            "likes",
            "dislikes",
            "author",
            "editor",
            "genre",
            "characters",
            "tags",
        )[:count]
    )
    return stories


def get_fresh_stories(count):
    exclude = ["draft", "prerelease"]
    stories = (
        Stories.objects.order_by("created_at")
        .exclude(status__in=exclude)
        .prefetch_related(
            "story_type",
            "language",
            "rating",
            "flags",
            "following",
            "likes",
            "dislikes",
            "author",
            "editor",
            "genre",
            "characters",
            "tags",
        )[:count]
    )
    return stories


def get_completed_stories(count):
    stories = Stories.objects.filter(status="completed").prefetch_related(
        "story_type",
        "language",
        "rating",
        "flags",
        "following",
        "likes",
        "dislikes",
        "author",
        "editor",
        "genre",
        "characters",
        "tags",
    )[:count]
    return stories


def get_updated_stories(count):
    stories = (
        Stories.objects.order_by("updated_at")
        .filter(status="active")
        .prefetch_related(
            "story_type",
            "language",
            "rating",
            "flags",
            "following",
            "likes",
            "dislikes",
            "author",
            "editor",
            "genre",
            "characters",
            "tags",
        )[:count]
    )
    return stories


def get_story_chapters(story: int, user: int):
    try:
        sponsor = Sponsors.objects.get(user=user, package__story=story)
        has_sponsorship = True
        package = sponsor.package
        advance = package.advance
    except Sponsors.DoesNotExist:
        has_sponsorship = False

    if has_sponsorship:
        released_chapters = Chapter.objects.filter(
            story=story, released_at__lte=datetime.now()
        )
        unreleased_chapters = Chapter.objects.filter(
            story=story, released_at__gt=datetime.now()
        )
        advance_chapters = unreleased_chapters[:advance]
        all_chapters = list(chain(released_chapters, advance_chapters))

    if not has_sponsorship:
        released_chapters = Chapter.objects.filter(
            story=story, released_at__lte=datetime.now()
        )
        all_chapters = released_chapters

    return all_chapters


from datetime import datetime


def can_view_chapter(user, chapter):
    try:
        sponsor = Sponsors.objects.get(user=user)
        package = Packages.objects.get(story=chapter.story, name=sponsor.package.name)
    except (Sponsors.DoesNotExist, Packages.DoesNotExist):
        return chapter.released_at <= datetime.now()

    # Get all the released chapters for this story
    released_chapters = Chapter.objects.filter(
        story=chapter.story, released_at__lte=datetime.now()
    ).order_by("position")

    # Get the position of the chapter in the list of released chapters
    position = released_chapters.values_list("position", flat=True).index(
        chapter.position
    )

    return position < package.advance or chapter.released_at <= datetime.now()


def get_chapter(user, story, chapter):
    # check if can view the chapter else end it there
    if can_view_chapter(user, chapter):
        chapter = (
            Chapter.objects.filter(status="active")
            .filter(story=story)
            .get(chapter=chapter)
        )
        return chapter


def get_user_profile(user):
    user = Users.objects.filter(username=user).prefetch_related(
        "authors", "editors", "authors__story"
    )
    return user


def get_reviews(story: str, chapter: str = None):
    parent = None
    reviews = (
        Review.objects.filter(~Q(status="pending") | ~Q(status="draft"))
        .filter(story__slug=story)
        .filter(chapter__slug=chapter)
        .filter(parent=parent)
        .annotate(chapters_count=Count("chapter"))
        .select_related(
            "story",
            "chapter",
            "user",
            "parent",
        )
        .prefetch_related(
            "story__author",
        )
        .order_by("created_at")
    )
    print(reviews)
    return reviews


def get_reviews_by_id(story: int, chapter: int = None):
    parent = None
    reviews = (
        Review.objects.filter(~Q(status="pending") | ~Q(status="draft"))
        .filter(story=story)
        .filter(chapter=chapter)
        .filter(parent=parent)
        .annotate(chapters_count=Count("chapter"))
        .select_related(
            "story",
            "chapter",
            "user",
            "parent",
        )
        .prefetch_related(
            "story__author",
        )
        .order_by("created_at")
    )
    print(reviews)
    return reviews


def create_review(story, chapter, text, user, parent):
    review = Review(story=story, chapter=chapter, user=user, text=text, parent=parent)
    review.save()
    return review


def update_review(id, text):
    review = Review.objects.get(id=id)
    review.text = text
    review.save(update_fields=["text"])
    return review


def get_review(id: int):
    review = Review.objects.filter(status="active").get(id=id)
    return review


def get_reviews(story, chapter):
    review = Review.objects.filter(story__slug=story, chapter__slug=chapter)
    return review


def delete_review(id: int):
    review = Review.objects.get(id=id)
    review.delete()
    return True


def train_recommendation():
    query = Stories.objects.values(
        "title",
        "slug",
        "abbreviation",
        "summary",
        "story_type",
        "following",
        "likes",
        "dislikes",
        "author",
        "language",
        "genre",
        "rating",
        "tags",
    )
    data = pd.DataFrame.from_records(list(query))
    predictor = mindsdb.Predictor(name="story_recommendation_predictor")
    predictor.learn(from_data=data, target="likes")


from django.db.models import CharField, Value as V
from django.db.models.functions import Concat


def predict_next_story(user, story_id):
    chapters = Chapter.objects.filter(story=story_id)
    story_text = chapters.aggregate(
        story_text=Concat("title", V(" "), "text", output_field=CharField())
    )["story_text"]

    data = {"user": user, "text": story_text}

    result = mindsdb.Predictor.predict(data)
    return result


def predict_next_stories(text):
    data = {"text": text}

    result = mindsdb.Predictor.predict(data)
    return result["story"]
