from django.contrib import admin

from .models import Disco


@admin.register(Disco)
class DiscoAdmin(admin.ModelAdmin):
    list_display = ('clave', 'nombre', 'cantdiscos',
                    'tipodisco', 'categoria', 'stock',
                    'existencia',)
    search_fields = ('clave', 'nombre',)
    list_filter = ('categoria', 'existencia',)
    list_editable = ('existencia',)
