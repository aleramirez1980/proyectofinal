
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
    path("registro/", include("registro.urls")),
    path('users/', include('users.urls')),
    path("vbc/", include("vbc.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
