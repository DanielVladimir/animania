from django.db.models import Q

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin

from ..models import Disco
from .serializers import DiscoSerializer


class DiscoLCAPIView(ListAPIView, CreateModelMixin):
    serializer_class = DiscoSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('clave', 'nombre',)

    def get_queryset(self):
        qs = Disco.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = filter(
                Q(clave__icontains=query)|
                Q(nombre__icontains=query)
            ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DiscoRUDAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'clave'
    serializer_class = DiscoSerializer

    def get_queryset(self):
        return Disco.objects.all()
