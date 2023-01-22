from django.contrib import admin
from django.urls import include, path
from .api import api
from django.conf import settings
from django.conf.urls.static import static
from two_factor.urls import urlpatterns as tf_urls
from django.conf.urls import handler404, handler500
from django.views import defaults as default_views

modules = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("ads/", include("modules.adverts.urls")),
    path("support/", include("modules.helpdesk.urls")),
    path("read/", include("modules.stories.urls")),
    path("author/", include("modules.stories.authors")),
    path("pages/", include("modules.pages.urls")),
    path("", include("modules.core.urls")),
    path("", include("modules.blog.urls")),
]

thirdparty = [
    path("search/", include("watson.urls", namespace="watson")),
    path("newsfeed/", include("newsfeed.urls", namespace="newsfeed")),
    path("cookies/", include("cookie_consent.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("flag/", include("flag.urls")),
    # path("unicorn/", include("django_unicorn.urls")),
    path("hijack/", include("hijack.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include(tf_urls)),
]

urlpatterns = modules + thirdparty

handler404 = "modules.core.views.error_404"
handler500 = "modules.core.views.error_500"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
