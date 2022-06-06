from django.urls import path
from . import views

app_name = 'story'
urlpatterns = [
    path('tags/<slug>-<int:id>/', views.ShowTag.as_view(), name='tag'),
    path('genre/<slug>-<int:id>/', views.ShowTag.as_view(), name='genre'),
    path('language/<slug>-<int:id>/', views.ShowTag.as_view(), name='language'),
    path('rating/<slug>-<int:id>/', views.ShowTag.as_view(), name='rating'),
    path('type/<slug>-<int:id>/', views.ShowTag.as_view(), name='type'),
    path('<str:type>/<slug>/', views.ShowStory.as_view(), name='show'),
    path('story/<int:id>/like/', views.StoryLike, name='like'),
    path('story/<int:id>/dislike/', views.StoryDisLike, name='dislike'),
    path('story/follow/<int:id>/', views.StoryFollow, name='follow'),
    path('story/bookmark/<int:id>/', views.StoryBookmark, name='bookmark'),
    path('<str:type>/<slug:story>/<slug:slug>/', views.ShowChapter.as_view(), name='read'),
]