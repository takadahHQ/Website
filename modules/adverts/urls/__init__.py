from django.urls import path
from django.conf.urls import include
from modules.adverts.urls import staff, user, author, personal

app_name = "adverts"
urlpatterns = [
    path("staff/adverts/", include((staff.urls, "staff"))),
    path("read/", include(user.urls)),
    path("author/", include((author.urls, "author"))),
    path("user/", include(personal.urls)),
]
