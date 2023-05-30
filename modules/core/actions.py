from modules.stories.actions.user import (
    get_bookmarked_stories,
    get_completed_stories,
    get_featured_stories,
    get_fresh_stories,
    get_updated_stories,
    get_user_histories,
    get_user_profile,
    get_weekly_stories,
    get_stories_by_type,
    get_unpublished_stories,
    get_profile,
    get_review_by_user,
)

# from modules.stories.models import Bookmark, History, Stories
from modules.core.models import Users


def homepage(count):
    stories = {
        "weekly": get_weekly_stories(count=count),
        "fresh": get_fresh_stories(count=count),
        "completed": get_completed_stories(count=count),
        "featured": get_featured_stories(count=count),
        "updated": get_updated_stories(count=count),
        "peotry": get_stories_by_type("poetry", count=count),
        "fanfiction": get_stories_by_type("fan-fiction", count=count),
        "nonfiction": get_stories_by_type("non-fiction", count=count),
        "fiction": get_stories_by_type("fiction", count=count),
        "plays": get_stories_by_type("plays", count=count),
        "webnovel": get_stories_by_type("web-novel", count=count),
        "prerelease": get_unpublished_stories(count=count),
    }
    return stories


def get_bookmarks(user):
    bookmarks = get_bookmarked_stories(user=user)
    return bookmarks


def get_histories(user):
    histories = get_user_histories(user=user)
    return histories


def get_users_profile(user):
    user = get_user_profile(user)
    return user


def get_profile(user):
    test = isinstance(user, int)
    if test:
        pass
    else:
        user = Users.objects.get_by_natural_key(username=user)

    bookmarks = get_bookmarked_stories(user)
    reviews = get_review_by_user(user)
    # user = get_user_profile(user)

    return bookmarks, reviews
