from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('<slug:category>/', views.CategoryListView.as_view(), name='category'),
    path('<slug:category>/<slug:slug>/', views.page, name='post'),
]