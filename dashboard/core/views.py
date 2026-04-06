from django.shortcuts import render


def home(request):
    context = {
        'titulo': 'Dashboard E-commerce',
        'usuario': 'Juan',
        'total_productos': 150,
        'ventas_hoy': 45,
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')
