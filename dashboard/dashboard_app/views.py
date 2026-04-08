from django.shortcuts import render
from django.db.models import Sum, Count, F
from .models import Venta, Cliente
from productos.models import Producto, Categoria


def panel_principal(request):
    stats = {
        'total_productos': Producto.objects.filter(activo=True).count(),
        'total_categorias': Categoria.objects.filter(activa=True).count(),
        'total_clientes': Cliente.objects.count(),
        'total_ventas': Venta.objects.count(),
    }
    ingresos = Venta.objects.aggregate(
        total=Sum(F('cantidad') * F('precio_unitario'))
    )['total'] or 0
    ultimas_ventas = Venta.objects.select_related('producto', 'cliente').order_by('-fecha')[:5]
    top_productos = (
        Producto.objects
        .annotate(total_vendido=Sum('ventas__cantidad'))
        .filter(total_vendido__isnull=False)
        .order_by('-total_vendido')[:5]
    )
    context = {
        'stats': stats,
        'ingresos': ingresos,
        'ultimas_ventas': ultimas_ventas,
        'top_productos': top_productos,
    }
    return render(request, 'dashboard_app/panel.html', context)


def resumen_ventas(request):
    ventas = Venta.objects.select_related('producto', 'cliente').all()
    return render(request, 'dashboard_app/ventas.html', {'ventas': ventas})


def ventas_por_año(request, año):
    ventas = Venta.objects.filter(fecha__year=año)
    total = sum(v.total for v in ventas)
    return render(request, 'dashboard_app/ventas_año.html', {
        'año': año,
        'total': total,
        'transacciones': ventas.count(),
    })
