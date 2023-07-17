from django.db.models import Count, Avg
from modules.stories.models.stories import Stories, Review
from django.db.models import OuterRef, Subquery
import random


def get_user_genre_preferences(user_id):
    # Get the genre preferences of the user based on their reviewed stories
    user_genre_preferences = (
        Stories.objects.filter(reviews__user=user_id)
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
    # Get the user's reviewed stories
    user_reviewed_stories = Stories.objects.filter(reviews__user=user_id)

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
            genre__in=user_reviewed_stories.values("genre"),
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

    # Step 3: Combine and shuffle the recommendations for final personalized recommendations
    combined_recommendations = list(favorite_stories) + list(
        content_based_recommendations
    )
    random.shuffle(combined_recommendations)

    return combined_recommendations[:10]
