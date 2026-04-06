from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.lista_productos, name='lista'),
    path('<int:id>/', views.detalle_producto, name='detalle'),
    path('categoria/<str:categoria>/', views.productos_por_categoria, name='por_categoria'),
    path('api/', views.api_productos, name='api_lista'),
    path('api/<int:id>/', views.api_producto, name='api_detalle'),
]
