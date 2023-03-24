from django.urls import path
from django.conf.urls import include
from modules.subscriptions.urls import staff, user, author

app_name = "sponsor"
urlpatterns = [
    path("staff/sponsorship/", include((staff.urls, "staff"))),
    path("sponsor/", include(user.urls)),
    path("author/", include((author.urls, "author"))),
]
