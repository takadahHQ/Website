from django.urls import path
from modules.stories.views import user as views

urls = [
    path("tags/<slug>/", views.ShowTag.as_view(), name="tag"),
    path("genre/<slug>/", views.ShowGenre.as_view(), name="genre"),
    path("language/<slug>/", views.ShowLanguage.as_view(), name="language"),
    path("rating/<slug>/", views.ShowRating.as_view(), name="rating"),
    path("type/<slug>/", views.ShowType.as_view(), name="type"),
    path("<str:type>/<slug>/", views.ShowStory.as_view(), name="show"),
    path("story/<int:id>/like/", views.StoryLike, name="like"),
    path("story/<int:id>/dislike/", views.StoryDisLike, name="dislike"),
    path("story/follow/<int:id>/", views.StoryFollow, name="follow"),
    path("story/bookmark/<int:id>/", views.StoryBookmark, name="bookmark"),
    path(
        "<str:type>/<slug:story>/<slug:slug>/", views.ShowChapter.as_view(), name="read"
    ),
]
