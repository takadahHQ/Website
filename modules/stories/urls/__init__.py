from django.urls import path
from django.conf.urls import include
from modules.stories.urls import staff, user, author

app_name = "stories"
urlpatterns = [
    path("staff/stories/", include((staff.urls, "staff"))),
    path("read/", include(user.urls)),
    path("author/", include((author.urls, "author"))),
]
