from django.urls import include, path
from . import views

app_name='core'

urlpatterns = [
    path('bookmark/', views.ShowBookmark.as_view(), name='bookmark'),
    path('history/', views.ShowHistory.as_view(), name='history'),
    path('history/<int:id>/delete/', views.DeleteHistory.as_view(), name='stop-reading'),
    path('accounts/register/', views.SignUpView.as_view(), name='register'),
    path('', views.index, name='index'),
]
