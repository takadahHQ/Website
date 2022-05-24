from django.urls import path, re_path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.page, name='page'),
    path('<str:path>/<slug:slug>/', views.page, name='page'),
]