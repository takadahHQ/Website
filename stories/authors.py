from django.urls import path
from . import views

app_name = 'author'
urlpatterns = [
    path('', views.storyDashboard.as_view(), name='dashboard'),
    path('list/', views.storyList.as_view(), name='list'),
    path('create/', views.createStory.as_view(), name='create'),
    path('story/<pk>/', views.viewStory.as_view(), name='show'),
    path('story/<pk>/update/', views.updateStory.as_view(), name='update'),
    path('story/<int:pk>/delete/', views.deleteStory.as_view(), name='delete'),
    path('story/<int:pk>/chapter/new/', views.createChapter.as_view(), name='createchapter'),
    path('story/<int:pk>/chapter/<slug:slug>/', views.updateChapter.as_view(), name='updatechapter'),
    path('story/<int:pk>/chapter/<slug:slug>/delete/', views.deleteChapter.as_view(), name='deletechapter'),
]