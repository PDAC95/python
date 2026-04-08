from django.contrib import admin
from .models import Venta, Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono', 'creado']
    search_fields = ['nombre', 'email']


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['producto', 'cliente', 'cantidad', 'precio_unitario', 'fecha']
    list_filter = ['fecha']
    search_fields = ['producto__nombre', 'cliente__nombre']
