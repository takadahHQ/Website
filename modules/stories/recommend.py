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
        Stories.objects.filter(id__in=Subquery(input_stories.values("id")))
        .values("genre")
        .annotate(count=Count("genre"))
    )
    return user_genre_preferences


def get_similar_users(user_id):
    # Find users with similar interests based on genre preferences and reviewed stories
    user_genre_preferences = get_user_genre_preferences(user_id)
    similar_users = []
    for genre_preference in user_genre_preferences:
        genre_stories = Stories.objects.filter(genre=genre_preference["genre"]).exclude(
            reviews__user=user_id
        )
        similar_users.extend(
            Review.objects.filter(story__in=genre_stories).values_list(
                "user", flat=True
            )
        )

    return list(set(similar_users))


def get_content_based_recommendations(user_id):
    # Get the user's reviewed, bookmarked and read stories
    reviewed_stories = get_reviewed_stories(user_id)
    bookmarked_stories = get_bookmarked_stories(user_id)
    historical_stories = get_historical_stories(user_id)
    input_stories = (
        list(reviewed_stories) + list(bookmarked_stories) + list(historical_stories)
    )
    random.shuffle(input_stories)

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

    # Calculate user's average review tone
    user_avg_tone = Review.objects.filter(user=user_id).aggregate(avg_tone=Avg("tone"))[
        "avg_tone"
    ]

    # Filter stories based on content-based criteria (length, reviews, tone)
    content_based_recommendations = (
        Stories.objects.filter(
            genre__in=input_stories.values("genre"),
            words__gte=genre_avg_length.filter(genre=OuterRef("genre")).values(
                "avg_length"
            )[:1],
            reviews__user__gte=genre_avg_reviews.filter(genre=OuterRef("genre")).values(
                "avg_reviews"
            )[:1],
            tone__gte=user_avg_tone,
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


def tiktok_style_recommendation(user_id):
    # Step 1: Get collaborative filtering recommendations
    similar_users = get_similar_users(user_id)
    favorite_stories = (
        Stories.objects.filter(reviews__user__in=similar_users)
        .annotate(likes_count=Count("reviews__user"))
        .order_by("-likes_count")[:10]
    )

    # Step 2: Get content-based recommendations
    content_based_recommendations = get_content_based_recommendations(user_id)

    # Step 3: Get personalized recommendations based on bookmarks and history
    bookmarked_stories = get_bookmarked_stories(user_id)
    historical_stories = get_historical_stories(user_id)

    # Combine and shuffle the recommendations for final personalized recommendations
    combined_recommendations = (
        list(favorite_stories)
        + list(content_based_recommendations)
        + list(bookmarked_stories)
        + list(historical_stories)
    )
    random.shuffle(combined_recommendations)

    return combined_recommendations[:10]
