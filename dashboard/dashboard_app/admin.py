from django.contrib import admin
from .models import Venta


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['producto', 'cantidad', 'precio_unitario', 'fecha']
    list_filter = ['fecha']
    search_fields = ['producto__nombre']
