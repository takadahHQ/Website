from django.urls import path
from modules.roadmap.views import user as views

urls = [
    path("", views.roadmap, name="feature_list"),
    path("<int:pk>/", views.FeatureDetailView.as_view(), name="feature_detail"),
    path("<int:pk>/vote/<str:action>", views.vote, name="vote"),
    path("<int:pk>/comment/", views.comments, name="comments"),
    path("reply/", views.comment, name="reply"),
    path("replies/<int:comment_id>/", views.replies, name="replies"),
]
