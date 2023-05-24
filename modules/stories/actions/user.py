from django.db.models import Q, Count, Sum, Prefetch
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from modules.stories.models import (
    Chapter,
    Stories,
    Bookmark,
    Language,
    Genre,
    Rating,
    Type,
    History,
)
from modules.core.models import Users
from modules.subscriptions.models import Sponsors, Packages
from modules.stories.models.review import Review
from django.urls import reverse

# import pandas as pd
from itertools import chain
from django.db.models import CharField, Value as V
from django.db.models.functions import Concat

# from timezone import timezone
from django.utils import timezone
from django.http import Http404

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
        .annotate(review_count=Count("reviews"))
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
            Prefetch(
                "chapters",
                queryset=Chapter.objects.filter(
                    released_at__lte=timezone.now(), status="active"
                ),
            ),
        )
        .get(slug=slug)
    )
    return story


def get_story_by_id(pk: int):
    story = Stories.objects.prefetch_related(
        "story_type",
        "language",
        "rating",
        "following",
        "likes",
        "dislikes",
        "author",
        # "bookmarks",
        "editor",
        "genre",
        "characters",
        "tags",
        Prefetch(
            "reviews",
            queryset=Review.objects.filter(parent=None, status="active"),
        ),
        "story__chapters",
        Prefetch(
            "chapters",
            queryset=Chapter.objects.filter(
                released_at__lte=timezone.now(), status="active"
            ),
        ),
    ).get(pk=pk)
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
    bookmark = Bookmark.objects.filter(story=story, user=user)
    if bookmark.exists():
        bookmark.delete()
    else:
        bookmark = Bookmark.objects.create(story=story, user=user)
    bookmarks = get_story_bookmarks(story=story)
    return bookmarks, story


def get_story_bookmarks(story):
    bookmarks = Bookmark.objects.filter(story=story.id)
    return bookmarks


def get_profile(user):
    test = isinstance(user, int)
    if test:
        pass
    else:
        user = Users.objects.get(username__iexact=user)

    bookmarks = get_bookmarked_stories(user)
    reviews = get_review_by_user(user)
    # user = get_user_profile(user)

    return bookmarks, reviews


def get_bookmarked_stories(user):
    # test = isinstance(user, int)
    # if test:
    #     pass
    # else:
    #     user = Users.objects.get(username=user)
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


# get list of stories type
def get_story_types():
    story_types = Type.objects.filter(status="active")
    return story_types


# get stories seperated by the type of story
def get_stories_by_type(story_type, count):
    exclude = ["draft", "prerelease"]
    stories = (
        Stories.objects.filter(story_type__slug=story_type)
        .order_by("created_at")
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
            story=story, status="active", released_at__lte=timezone.now()
        )
        unreleased_chapters = Chapter.objects.filter(
            story=story, status="active", released_at__gt=timezone.now()
        )
        advance_chapters = unreleased_chapters[:advance]
        all_chapters = list(chain(released_chapters, advance_chapters))

    if not has_sponsorship:
        released_chapters = Chapter.objects.filter(
            story=story, status="active", released_at__lte=timezone.now()
        )
        all_chapters = released_chapters

    return all_chapters


def can_view_chapter(user: int, chapter: str):
    try:
        chapter = Chapter.objects.get(slug=chapter)
        sponsor = Sponsors.objects.get(user=user)
        package = Packages.objects.get(story=chapter.story, name=sponsor.package.name)
    except (Sponsors.DoesNotExist, Packages.DoesNotExist):
        return chapter.released_at <= timezone.now()

    # Get all the released chapters for this story
    released_chapters = Chapter.objects.filter(
        story=chapter.story, status="active", released_at__lte=timezone.now()
    ).order_by("position")

    # Get the position of the chapter in the list of released chapters
    position = released_chapters.values_list("position", flat=True).index(
        chapter.position
    )

    return position < package.advance or chapter.released_at <= timezone.now()


def get_chapter(story: any, chapter: any, user: any = None):
    chapter = Chapter.objects.get(story__slug=story, slug=chapter)
    if not chapter.can_view(user=user):
        raise Http404(
            "This chapter does not exist or your might need to subscribe for access."
        )
    if chapter.is_last():
        chapter.prefetch_related(
            "story__packages",
        )
    previous_chapter, next_chapter = chapter.get_previous_and_next_chapters(user=user)
    return chapter  # , previous_chapter, next_chapter


def get_chapter_by_id(chapter: int, user: any = None):
    chapter = Chapter.objects.get(id=chapter)
    if not chapter.can_view(user=user):
        raise Http404(
            "This chapter does not exist or your might need to subscribe for access."
        )
    if chapter.is_last():
        chapter.prefetch_related(
            "story__packages",
        )
    previous_chapter, next_chapter = chapter.get_previous_and_next_chapters(user=user)
    return chapter  # , previous_chapter, next_chapter


def get_user_profile(user):
    user = Users.objects.filter(username__iexact=user).prefetch_related(
        "authors", "editors", "authors__story"
    )
    return user


def create_review(story, chapter, text, user, parent):
    review = Review(story=story, chapter=chapter, user=user, text=text, parent=parent)
    review.save()
    return review


def update_review(id, text):
    review = Review.objects.get(id=id)
    review.text = text
    review.save(update_fields=["text"])
    return review


# def get_review(id: int):
#     review = Review.objects.filter(status="active").get(id=id)
#     return review
def get_reviews_by_id(review: int):
    review = (
        Review.objects.filter(~Q(status="pending") | ~Q(status="draft"))
        .select_related(
            "story",
            "chapter",
            "user",
            # "parent",
        )
        .prefetch_related(
            "story__author",
        )
        .get(id=review)
    )
    return review


def get_review_by_user(user):
    reviews = (
        Review.objects.filter(status="active")
        .filter(user=user)
        .select_related("story", "user")
        .prefetch_related("story__author")
        .order_by("-created_at")
    )
    return reviews


def get_reviews(story, chapter):
    reviews = (
        Review.objects.filter(status="active")
        .select_related("story", "user")
        .prefetch_related("story__author")
        .order_by("-created_at")
    )
    if chapter:
        reviews = reviews.filter(story__slug=story, chapter__slug=chapter)
    else:
        reviews = reviews.filter(story__slug=story)
    count = reviews.count()
    reviews = reviews.filter(parent=None)
    return reviews, count


def remove_review(id: int):
    review = Review.objects.get(id=id)
    review.delete()
    return True


def get_packages(story, chapter):
    packages = (
        Packages.objects.filter(story__slug=story)
        .select_related("story")
        .annotate(counts=Count("sponsor"))
    )
    return packages


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
    # data = pd.DataFrame.from_records(list(query))
    predictor = mindsdb.Predictor(name="story_recommendation_predictor")
    predictor.learn(from_data=data, target="likes")


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
