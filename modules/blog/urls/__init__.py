from django.urls import path
from django.conf.urls import include
from modules.blog.urls import staff, user

app_name = "accounts"
urlpatterns = [
    path("staff/blog", include(staff.urls)),
    path("blog", include(user.urls)),
]
