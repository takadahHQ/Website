from django.urls import path
from . import views

app_name = 'author'
urlpatterns = [
    path('', views.storyDashboard.as_view(), name='dashboard'),
    path('list/', views.storyList.as_view(), name='list'),
    path('add/<int:pk>/author/', views.add_author, name='add-author'),
    path('show/<int:pk>/author/', views.detail_author, name='detail-author'),
    path('update/<int:pk>/author/', views.update_author, name='update-author'),
    path('delete/<int:pk>/author/', views.delete_author, name='delete-author'),
    path('add/editor/', views.add_editor, name='add-editor'),
    path('add/character/', views.add_character, name='add-character'),
    path('story/new/', views.createStory.as_view(), name='create'),
    path('story/<int:pk>/view/', views.viewStory.as_view(), name='show'),
    path('story/<int:pk>/update/', views.updateStory.as_view(), name='update'),
    path('story/<int:pk>/delete/', views.deleteStory.as_view(), name='delete'),
    path('story/<int:pk>/chapter/new/', views.createChapter.as_view(), name='create-chapter'),
    path('story/<int:pk>/chapter/<slug:slug>/update/', views.updateChapter.as_view(), name='update-chapter'),
    path('story/<int:pk>/chapter/<slug:slug>/delete/', views.deleteChapter.as_view(), name='delete-chapter'),
]