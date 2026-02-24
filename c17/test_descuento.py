import pytest
from descuento import calcular_descuento


class TestCalcularDescuento:

    def test_descuento_normal(self):
        """20% de descuento en $100 = $80"""
        assert calcular_descuento(100, 20) == 80

    def test_descuento_50_porciento(self):
        """50% de descuento"""
        assert calcular_descuento(200, 50) == 100

    def test_sin_descuento(self):
        """0% descuento = precio original"""
        assert calcular_descuento(100, 0) == 100

    def test_descuento_total(self):
        """100% descuento = gratis"""
        assert calcular_descuento(100, 100) == 0

    def test_precio_negativo_error(self):
        """Precio negativo debe lanzar ValueError"""
        with pytest.raises(ValueError):
            calcular_descuento(-50, 10)

    def test_porcentaje_mayor_100_error(self):
        """Porcentaje > 100 debe lanzar ValueError"""
        with pytest.raises(ValueError):
            calcular_descuento(100, 150)

    def test_porcentaje_negativo_error(self):
        """Porcentaje negativo debe lanzar ValueError"""
        with pytest.raises(ValueError):
            calcular_descuento(100, -10)

    def test_precio_cero(self):
        """Precio 0 con cualquier descuento = 0"""
        assert calcular_descuento(0, 50) == 0
