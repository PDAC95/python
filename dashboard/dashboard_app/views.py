from django.shortcuts import render
from django.db.models import Sum, Count
from .models import Venta
from productos.models import Producto, Categoria


def panel_principal(request):
    total_productos = Producto.objects.filter(activo=True).count()
    total_categorias = Categoria.objects.filter(activa=True).count()
    total_ventas = Venta.objects.count()
    return render(request, 'dashboard_app/panel.html', {
        'total_productos': total_productos,
        'total_categorias': total_categorias,
        'total_ventas': total_ventas,
    })


def resumen_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'dashboard_app/ventas.html', {'ventas': ventas})


def ventas_por_año(request, año):
    ventas = Venta.objects.filter(fecha__year=año)
    total = sum(v.total for v in ventas)
    return render(request, 'dashboard_app/ventas_año.html', {
        'año': año,
        'total': total,
        'transacciones': ventas.count(),
    })
