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
    path(
        "<str:type>/<slug:story>/<slug:slug>/", views.ShowChapter.as_view(), name="read"
    ),
    path("add/<int:story>/<int:chapter>/review/", views.save_review, name="add-review"),
    path(
        "update/<int:story>/<int:chapter>/review/",
        views.update_review,
        name="update-review",
    ),
    path("show/<int:review>/review/", views.detail_review, name="detail-review"),
    path("delete/<int:review>/review/", views.delete_review, name="delete-review"),
]
