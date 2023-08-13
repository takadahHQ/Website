from django.urls import path
from django.conf.urls import include
from modules.adverts.urls import staff, user, publisher, personal

app_name = "adverts"
urlpatterns = [
    path("staff/", include((staff.urls, "staff"))),
    path("", include(user.urls)),
    path("publisher/", include((publisher.urls, "publisher"))),
    # path("user/", include(personal.urls)),
]
