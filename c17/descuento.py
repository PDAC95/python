"""
Función de descuento - Para ejercicio 2
"""


def calcular_descuento(precio, porcentaje):
    """
    Calcula precio con descuento.

    Args:
        precio: Precio original (debe ser >= 0)
        porcentaje: Porcentaje de descuento (0-100)

    Returns:
        Precio con descuento aplicado

    Raises:
        ValueError: Si precio es negativo o porcentaje fuera de rango
    """
    if precio < 0:
        raise ValueError("Precio no puede ser negativo")
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("Porcentaje debe ser entre 0 y 100")
    return precio * (1 - porcentaje / 100)
