from modules.subscriptions.views import author as views

from django.urls import include, path, register_converter
from modules.stories.converter import StoryIdConverter

register_converter(StoryIdConverter, "story")
app_name = "author"
urls = [
    # Package URLs
    path(
        "story/<story:story>/",
        include(
            [
                path(
                    "packages/",
                    views.PackageListView.as_view(),
                    name="package-list",
                ),
                path(
                    "packages/new/",
                    views.PackageCreateView.as_view(),
                    name="package-create",
                ),
                path(
                    "packages/<int:pk>/edit/",
                    views.PackageUpdateView.as_view(),
                    name="package-update",
                ),
                path(
                    "packages/<int:pk>/delete/",
                    views.PackageDeleteView.as_view(),
                    name="package-delete",
                ),
                path(
                    "sponsors/",
                    views.SponsorListView.as_view(),
                    name="sponsor-list",
                ),
            ]
        ),
    )
]
