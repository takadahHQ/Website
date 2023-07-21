from django.urls import path
from modules.stories.views import user as views

urls = [
    path("tags/<slug>/", views.ShowTag.as_view(), name="tag"),
    path("genre/<slug>/", views.ShowGenre.as_view(), name="genre"),
    path("language/<slug>/", views.ShowLanguage.as_view(), name="language"),
    path("rating/<slug>/", views.ShowRating.as_view(), name="rating"),
    path("type/<slug>/", views.ShowType.as_view(), name="type"),
    path("<str:type>/<slug>/", views.showStory, name="show"),
    path("story/<int:id>/like/", views.storyLike, name="like"),
    path("story/<int:id>/dislike/", views.storyDisLike, name="dislike"),
    path("story/follow/<int:id>/", views.storyFollow, name="follow"),
    path("story/bookmark/<int:id>/", views.storyBookmark, name="bookmark"),
    path("review/add/<int:story>/<int:chapter>/", views.save_review, name="add-review"),
    path(
        "review/show/<int:story>/<int:chapter>/",
        views.refresh_reviews,
        name="show-review",
    ),
    path(
        "review/update/<int:review>/",
        views.update_review,
        name="update-review",
    ),
    path("review/reply/<int:review>/", views.reply_review, name="reply-review"),
    path("review/show/<int:review>/", views.detail_review, name="detail-review"),
    path("review/delete/<int:review>/", views.delete_review, name="delete-review"),
    path(
        "<str:type>/<slug:story>/<slug:slug>/", views.ShowChapter.as_view(), name="read"
    ),
    path("populate-model", views.populate_model, name="populate"),
    path("services", views.create_services_for_stories_view, name="services"),
]
