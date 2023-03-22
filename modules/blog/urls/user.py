from django.urls import path
from modules.blog.views import user

urls = [
    # blog index
    path("", user.PostListView.as_view(), name="list"),
    # path("/aaa", user.view_a, name="user.view_a"),
    # blog category
    path("<slug:category>/", user.CategoryListView.as_view(), name="category"),
    # blog tags
    # blog post
    path("<slug:category>/<slug:slug>/", user.page, name="post"),
]
