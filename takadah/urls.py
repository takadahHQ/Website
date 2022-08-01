from django.contrib import admin
from django.urls import include, path
from .api import api
from django.conf import settings
from django.conf.urls.static import static
from two_factor.urls import urlpatterns as tf_urls


urlpatterns = [
    path('report/', include('reports.urls')),
    path('ads/', include('adverts.urls')),
    path('admin/', admin.site.urls),
    #path("api/", api.urls),
    # path("unicorn/", include("django_unicorn.urls")),
    path('hijack/', include('hijack.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('flag/', include('flag.urls')),
    path('support/', include('helpdesk.urls')),
    path('cookies/', include('cookie_consent.urls')),
    path('blog/', include('blog.urls')),
    path('read/', include('stories.urls')),
    path('author/', include('stories.authors')),
    path('pages/', include('pages.urls')),
    path('search/', include("watson.urls", namespace="watson")),
    path('', include('core.urls')),
    path('', include(tf_urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
