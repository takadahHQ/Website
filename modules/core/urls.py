from django.urls import include, path
from . import views

app_name = "core"

urlpatterns = [
    path("bookmark/", views.ShowBookmark.as_view(), name="bookmark"),
    path("history/", views.ShowHistory.as_view(), name="history"),
    path(
        "history/<int:id>/delete/", views.DeleteHistory.as_view(), name="stop-reading"
    ),
    path("accounts/register/", views.SignUpView.as_view(), name="register"),
    path("a/<str:username>/", views.AuthorView.as_view(), name="author"),
    path("generated.css", views.generatedCss, name="stylesheet"),
    path("", views.index, name="index"),
]
