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
    path("pricing/", views.FeeView.as_view(), name="pricing"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("careers/", views.CareersView.as_view(), name="careers"),
    # path("history/", views.ShowHistory.as_view(), name="history"),
    path("populate", views.populate_model, name="populate"),
]
