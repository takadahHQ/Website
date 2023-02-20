from django.urls import path
from modules.subscriptions.views import author as views

app_name = "author"
urls = [
    # Package URLs
    path(
        "<str:type>/<story>/packages/",
        views.PackageListView.as_view(),
        name="package-list",
    ),
    path(
        "<str:type>/<story>/packages/new/",
        views.PackageCreateView.as_view(),
        name="package-create",
    ),
    path(
        "<str:type>/<story>/packages/<int:pk>/edit/",
        views.PackageUpdateView.as_view(),
        name="package-update",
    ),
    path(
        "<str:type>/<story>/packages/<int:pk>/delete/",
        views.PackageDeleteView.as_view(),
        name="package-delete",
    ),
    path(
        "<str:type>/<story>/sponsors/",
        views.SponsorListView.as_view(),
        name="sponsor-list",
    ),
]
