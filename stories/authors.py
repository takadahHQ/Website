from django.urls import path
from . import views

app_name = 'author'
urlpatterns = [
    path('', views.storyDashboard.as_view(), name='dashboard'),
    path('list/', views.storyList.as_view(), name='list'),
    path('create/', views.createStory.as_view(), name='create'),
    path('add/author/<int:pk>/', views.save_author, name='add-author'),
    path('add/editor/', views.add_editor, name='add-editor'),
    path('add/character/', views.add_character, name='add-character'),
    path('story/<pk>/view/', views.viewStory.as_view(), name='show'),
    path('story/<pk>/update/', views.updateStory.as_view(), name='update'),
    path('story/<int:pk>/delete/', views.deleteStory.as_view(), name='delete'),
    path('story/<int:pk>/chapter/new/', views.createChapter.as_view(), name='create-chapter'),
    path('story/<int:pk>/chapter/<slug:slug>/update', views.updateChapter.as_view(), name='update-chapter'),
    path('story/<int:pk>/chapter/<slug:slug>/delete/', views.deleteChapter.as_view(), name='delete-chapter'),
]