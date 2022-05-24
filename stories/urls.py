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
    path('<str:type>/<slug:story>/<slug:slug>/', views.ShowChapter.as_view(), name='read'),
]