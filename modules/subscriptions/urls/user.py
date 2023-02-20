from django.urls import path
from modules.subscriptions.views import user as views

urls = [
    path(
        "<str:type>/<story>/sponsors/",
        views.SponsorListView.as_view(),
        name="sponsor-list",
    ),
    path(
        "<str:type>/<story>/sponsors/new/",
        views.SponsorCreateView.as_view(),
        name="sponsor-create",
    ),
    path(
        "<str:type>/<story>/sponsors/<int:pk>/edit/",
        views.SponsorUpdateView.as_view(),
        name="sponsor-update",
    ),
    path(
        "<str:type>/<story>/sponsors/<int:pk>/delete/",
        views.SponsorDeleteView.as_view(),
        name="sponsor-delete",
    ),
]
