from django.urls import include, path

from .views import *

app_name = 'api-discos'

urlpatterns = [
    path('', DiscoLCAPIView.as_view(), name="lista_crear_disco"),
    path('<str:clave>/', DiscoRUDAPIView.as_view(), name="detalle_modificar_borrar_disco"),
]
