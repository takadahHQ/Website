from django.urls import path
from modules.subscriptions.views import user as views

urls = [
    path("sponsors/", views.SponsorListView.as_view(), name="sponsor-list"),
    path("sponsors/new/", views.SponsorCreateView.as_view(), name="sponsor-create"),
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
