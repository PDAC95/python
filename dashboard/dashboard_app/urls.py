from django.urls import path
from . import views

app_name = 'dashboard_app'

urlpatterns = [
    path('', views.panel_principal, name='panel'),
    path('ventas/', views.resumen_ventas, name='ventas'),
    path('ventas/<int:año>/', views.ventas_por_año, name='ventas_año'),
]
