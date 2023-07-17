from django.db.models import Count, Avg, OuterRef, Q, Subquery
from modules.stories.models.stories import Stories, Review
import random


def get_user_genre_preferences(user_id):
    # Get the user's reviewed, bookmarked, and read stories
    reviewed_stories = get_reviewed_stories(user_id)
    bookmarked_stories = get_bookmarked_stories(user_id)
    historical_stories = get_historical_stories(user_id)

    # Combine all interactions to get the user's input stories
    input_stories = (
        list(reviewed_stories) + list(bookmarked_stories) + list(historical_stories)
    )

    # Calculate the user's genre preferences based on their interactions
    user_genre_preferences = (
        Stories.objects.filter(id__in=[story.id for story in input_stories])
        .values("genre")
        .annotate(count=Count("genre"))
    )
    return user_genre_preferences


def get_similar_users(user_id):
    # Find users with similar interests based on genre preferences and reviewed stories
    user_genre_preferences = get_user_genre_preferences(user_id)
    similar_users = Review.objects.filter(
        story__genre__in=[genre["genre"] for genre in user_genre_preferences]
    )
    similar_users = (
        similar_users.exclude(user=user_id).values_list("user", flat=True).distinct()
    )

    return list(similar_users)


def get_collaborative_filtering_recommendations(user_id):
    similar_users = get_similar_users(user_id)
    collaborative_filtering_recommendations = (
        Stories.objects.filter(reviews__user__in=similar_users)
        .annotate(likes_count=Count("reviews__user"))
        .order_by("-likes_count")[:10]
    )
    return collaborative_filtering_recommendations


def get_content_based_recommendations(user_id, story_id=None):
    if user_id:
        # Get the user's reviewed, bookmarked, and read stories
        input_stories = (
            get_reviewed_stories(user_id)
            | get_bookmarked_stories(user_id)
            | get_historical_stories(user_id)
        )
    elif story_id:
        # Get the current story based on story_id for context-based recommendations
        input_stories = Stories.objects.filter(id=story_id)

    # Calculate average story length and number of reviews by genre
    genre_avg_length = (
        Stories.objects.values("genre")
        .annotate(avg_length=Avg("words"))
        .order_by("genre")
    )
    genre_avg_reviews = (
        Stories.objects.values("genre")
        .annotate(avg_reviews=Avg("reviews__user"))
        .order_by("genre")
    )

    # Filter stories based on content-based criteria (length, reviews, !tone)
    content_based_recommendations = (
        Stories.objects.filter(
            genre__in=input_stories.values("genre"),
            words__gte=genre_avg_length.filter(genre=OuterRef("genre")).values(
                "avg_length"
            )[:1],
            reviews__user__gte=genre_avg_reviews.filter(genre=OuterRef("genre")).values(
                "avg_reviews"
            )[:1],
        )
        .exclude(reviews__user=user_id)
        .order_by("?")[:10]
    )

    return content_based_recommendations


def get_bookmarked_stories(user_id):
    # Get stories that the user has bookmarked
    bookmarked_stories = Stories.objects.filter(bookmarked__user=user_id)
    return bookmarked_stories


def get_reviewed_stories(user_id):
    # Get stories that the user has reviewed
    reviewed_stories = Stories.objects.filter(reviews__user=user_id)
    return reviewed_stories


def get_historical_stories(user_id):
    # Get stories that the user has read in the history
    historical_stories = Stories.objects.filter(history__user=user_id)
    return historical_stories


def tiktok_style_recommendation(user_id=None, story_id=None):
    if user_id:
        # Step 1: Get collaborative filtering recommendations
        collaborative_filtering_recommendations = (
            get_collaborative_filtering_recommendations(user_id)
        )
        # Step 2: Get content-based recommendations
        content_based_recommendations = get_content_based_recommendations(user_id)

        # Combine and shuffle the recommendations for final personalized recommendations
        combined_recommendations = list(collaborative_filtering_recommendations) + list(
            content_based_recommendations
        )
        random.shuffle(combined_recommendations)

        return combined_recommendations[:10]
    elif story_id:
        # When not logged in, provide context-based recommendations based on the current story
        content_based_recommendations = get_content_based_recommendations(
            user_id=None, story_id=story_id
        )[:10]
        return content_based_recommendations
    else:
        return []
