from django.contrib import admin
from django.urls import include, path

import views

urlpatterns = [
    path("<service_uuid>/pixel.gif", views.PixelView.as_view(), name="endpoint_pixel"),
    path(
        "<service_uuid>/script.js", views.ScriptView.as_view(), name="endpoint_script"
    ),
    path(
        "<service_uuid>/<identifier>/pixel.gif",
        views.PixelView.as_view(),
        name="endpoint_pixel_id",
    ),
    path(
        "<service_uuid>/<identifier>/script.js",
        views.ScriptView.as_view(),
        name="endpoint_script_id",
    ),
]
