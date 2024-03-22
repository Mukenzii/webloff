from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from bazasite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bazaapp.urls'))
]
admin.site.index_title = 'DizaynBaza Admin'
admin.site_header = "Toshkentlikman"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_MEDIA)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
