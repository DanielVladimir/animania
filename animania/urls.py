from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    ### ADMIN DE DJANGO ###
    path('admin/', admin.site.urls),

    ### API REST ###
    path('api/v1/discos/', include('modulos.discos.api.urls', namespace='api-discos')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
