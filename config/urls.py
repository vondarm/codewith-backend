from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from config.core import views as core_views

urlpatterns = [
    path("", core_views.index),
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path('api/auth/', include('users.urls')),
    path("api/workspace/", include("workspaces.urls")),
    path("api/workspace_member/", include("workspace_members.urls"))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
