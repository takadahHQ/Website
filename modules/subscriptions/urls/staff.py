from django.urls import path
from modules.subscriptions.views.staff import staff

urls = [
    path("sponsors/", staff.SponsorListView.as_view(), name="sponsor-list"),
    path("sponsors/new/", staff.SponsorCreateView.as_view(), name="sponsor-create"),
    path(
        "sponsors/<int:pk>/edit/",
        staff.SponsorUpdateView.as_view(),
        name="sponsor-update",
    ),
    path(
        "sponsors/<int:pk>/delete/",
        staff.SponsorDeleteView.as_view(),
        name="sponsor-delete",
    ),
    # Package URLs
    path("packages/", staff.PackageListView.as_view(), name="package-list"),
    path("packages/new/", staff.PackageCreateView.as_view(), name="package-create"),
    path(
        "packages/<int:pk>/edit/",
        staff.PackageUpdateView.as_view(),
        name="package-update",
    ),
    path(
        "packages/<int:pk>/delete/",
        staff.PackageDeleteView.as_view(),
        name="package-delete",
    ),
]
