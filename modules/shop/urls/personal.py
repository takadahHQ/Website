from django.urls import path
from modules.stories.views import user as views

urls = [
    path("", views.userDashboard.as_view(), name="index"),
    path("dashboard/", views.userDashboard.as_view(), name="dashboard"),
]
