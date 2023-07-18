# from django.db.models import Count, Avg, Sum, OuterRef, Q, Subquery
from django.db.models import (
    Count,
    Avg,
    OuterRef,
    Subquery,
    Sum,
    Case,
    When,
    IntegerField,
    F,
)
from modules.stories.models import Stories, Review, Chapter
from django.utils import timezone
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


# def get_word_count(story):
#     active_chapters = story.chapters.filter(
#         status="active", released_at__lte=timezone.now()
#     )
#     total_word_count = sum(chapter.words for chapter in active_chapters)
#     return total_word_count


def get_word_count_annotation():
    # Annotate each story with its total word count from active chapters
    # return Sum(
    #     Case(
    #         When(
    #             chapters__status="active",
    #             chapters__released_at__lte=timezone.now(),
    #             then=F("chapters__words"),
    #         ),
    #         default=0,
    #         output_field=IntegerField(),
    #     )
    # )
    # Annotate each story with its total word count from active chapters
    return Subquery(
        Chapter.objects.filter(
            story_id=OuterRef("pk"), status="active", released_at__lte=timezone.now()
        )
        .values("story_id")
        .annotate(total_words=Sum("words"))
        .values("total_words")
    )


def get_collaborative_filtering_recommendations(user_id):
    similar_users = get_similar_users(user_id)
    collaborative_filtering_recommendations = (
        Stories.objects.filter(reviews__user__in=similar_users)
        .annotate(likes_count=Count("reviews__user"))
        .distinct()
        .order_by("-likes_count")[:10]
    )
    return collaborative_filtering_recommendations


def get_content_based_recommendations(user_id=None, story_id=None):
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
        .annotate(avg_length=Avg(get_word_count_annotation()))
        .order_by("genre")
    )

    genre_avg_reviews = (
        Stories.objects.values("genre")
        .annotate(avg_reviews=Avg("reviews__user"))
        .order_by("genre")
    )

    # Annotate stories with the total word count from active chapters
    annotated_stories = Stories.objects.annotate(
        total_words=Sum(
            Case(
                When(
                    chapters__status="active",
                    chapters__released_at__lte=timezone.now(),
                    then=F("chapters__words"),
                ),
                default=0,
                output_field=IntegerField(),
            )
        )
    )
    # Filter stories based on content-based criteria (length, reviews)
    content_based_recommendations = (
        annotated_stories.filter(
            genre__in=input_stories.values("genre"),
            # reviews__user__gte=genre_avg_reviews.filter(genre=OuterRef("genre")).values(
            #     "avg_reviews"
            # ),
            total_words__gte=genre_avg_length.filter(genre=OuterRef("genre")).values(
                "avg_length"
            )[:1],
        )
        .annotate(total_words=Sum("chapters__words"))
        .distinct()
        # .exclude(reviews__user=user_id)
        .order_by("?")[:10]
    )
    content_based_recommendations = list(dict.fromkeys(content_based_recommendations))
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


def recommend(user_id=None, story_id=None):
    if user_id:
        # Step 1: Get collaborative filtering recommendations
        collaborative_filtering_recommendations = (
            get_collaborative_filtering_recommendations(user_id)
        )
        # Step 2: Get content-based recommendations
        content_based_recommendations = get_content_based_recommendations(
            user_id, story_id=None
        )

        # Combine and shuffle the recommendations for final personalized recommendations
        combined_recommendations = list(collaborative_filtering_recommendations) + list(
            set(list(content_based_recommendations))
            - set(list(collaborative_filtering_recommendations))
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
