from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria


def lista_productos(request):
    productos = Producto.objects.filter(activo=True)
    return render(request, 'productos/lista.html', {'productos': productos})


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos/detalle.html', {'producto': producto})


def productos_por_categoria(request, categoria):
    cat = get_object_or_404(Categoria, nombre__iexact=categoria)
    productos = Producto.objects.filter(categoria=cat, activo=True)
    return render(request, 'productos/categoria.html', {
        'categoria': cat.nombre,
        'productos': productos,
    })


def api_productos(request):
    productos = list(Producto.objects.filter(activo=True).values(
        'id', 'nombre', 'precio', 'stock', 'categoria__nombre'
    ))
    return JsonResponse(productos, safe=False)


def api_producto(request, id):
    try:
        producto = Producto.objects.values(
            'id', 'nombre', 'precio', 'stock', 'descripcion', 'categoria__nombre'
        ).get(id=id)
        return JsonResponse(producto)
    except Producto.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)
