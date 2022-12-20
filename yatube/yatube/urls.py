from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('ski_resort/', include('ski_resort.urls', namespace='ski_resort')),
    path('captcha/', include('captcha.urls')),
    path('about/', include('about.urls', namespace='about'))
]

handler404 = "core.views.page_not_found"
handler403 = "core.views.csrf_failure"
handler500 = "core.views.server_error"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
