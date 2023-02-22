from modules.subscriptions.views import user as views

from django.urls import include, path, register_converter
from modules.stories.converter import StoryIdConverter

register_converter(StoryIdConverter, "story")
#        "<str:type>/<story>/",
urls = [
    path(
        "<story:story>/",
        include(
            [
                path(
                    "sponsors/",
                    views.SponsorListView.as_view(),
                    name="sponsor-list",
                ),
                path(
                    "sponsors/new/",
                    views.SponsorCreateView.as_view(),
                    name="sponsor-create",
                ),
                path(
                    "sponsors/<int:pk>/edit/",
                    views.SponsorUpdateView.as_view(),
                    name="sponsor-update",
                ),
                path(
                    "sponsors/<int:pk>/delete/",
                    views.SponsorDeleteView.as_view(),
                    name="sponsor-delete",
                ),
            ]
        ),
    )
]
