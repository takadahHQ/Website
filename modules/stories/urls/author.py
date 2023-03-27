from django.urls import include, path, register_converter
from modules.stories.converter import StoryIdConverter

register_converter(StoryIdConverter, "story")

from modules.stories.views import author as views

app_name = "author"
urls = [
    path("", views.storyDashboard.as_view(), name="dashboard"),
    path("list/", views.storyList.as_view(), name="list"),
    path("add/<story:pk>/author/", views.save_author, name="add-author"),
    path("show/<story:pk>/author/", views.detail_author, name="detail-author"),
    path("update/<story:pk>/author/", views.update_author, name="update-author"),
    path("delete/<story:pk>/author/", views.delete_author, name="delete-author"),
    path("add/editor/", views.add_editor, name="add-editor"),
    path("add/character/", views.add_character, name="add-character"),
    path("story/new/", views.StoriesCreateView.as_view(), name="create"),
    path("story/<story:pk>/view/", views.viewStory.as_view(), name="show"),
    path("story/<story:pk>/update/", views.updateStory.as_view(), name="update"),
    path("story/<story:pk>/delete/", views.deleteStory.as_view(), name="delete"),
    path(
        "story/<story:pk>/chapter/new/",
        views.createChapter.as_view(),
        name="create-chapter",
    ),
    path(
        "story/<story:pk>/chapter/<slug:slug>/preview/",
        views.showChapter.as_view(),
        name="preview-chapter",
    ),
    path(
        "story/<story:pk>/chapter/<slug:slug>/update/",
        views.updateChapter.as_view(),
        name="update-chapter",
    ),
    path(
        "story/<story:pk>/chapter/<slug:slug>/delete/",
        views.deleteChapter.as_view(),
        name="delete-chapter",
    ),
]
