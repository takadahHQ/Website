from django.urls import path
from django.conf.urls import include
from modules.roadmap.urls import staff, user, author

app_name = "roadmap"
urlpatterns = [
    path("staff/roadmap/", include((staff.urls, "staff"))),
    path("", include(user.urls)),
]
