"""
EJERCICIO: Escribe tests para calcular_descuento

Instrucciones:
1. Importa pytest y calcular_descuento
2. Crea tests para cada caso listado abajo
3. Ejecuta: pytest ejercicio_tests.py -v

Casos a testear:
- Descuento normal (precio=100, porcentaje=20 -> 80)
- Sin descuento (porcentaje=0)
- Descuento total (porcentaje=100 -> 0)
- Precio negativo debe lanzar ValueError
- Porcentaje mayor a 100 debe lanzar ValueError
- Porcentaje negativo debe lanzar ValueError
- Precio cero con descuento
"""
import pytest
from descuento import calcular_descuento


# TODO: Escribe tus tests aquí

def test_descuento_normal():
    # precio=100, porcentaje=20 debe dar 80
    pass


def test_sin_descuento():
    # porcentaje=0 debe dar el precio original
    pass


def test_descuento_total():
    # porcentaje=100 debe dar 0
    pass


def test_precio_negativo_error():
    # precio negativo debe lanzar ValueError
    # Pista: usa with pytest.raises(ValueError):
    pass


def test_porcentaje_mayor_100_error():
    # porcentaje > 100 debe lanzar ValueError
    pass


def test_porcentaje_negativo_error():
    # porcentaje < 0 debe lanzar ValueError
    pass


def test_precio_cero():
    # precio=0 con cualquier descuento debe dar 0
    pass
