"""
Clase 20 - Herencia: EJERCICIO 2 — Template para alumnos
=========================================================
Archivo: ejercicio2_template.py

Instrucciones:
- Completa las clases siguiendo los comentarios # TODO:
- Figura es la clase PADRE
- Rectangulo y Circulo son clases HIJAS
- Usa super().__init__() y super().describir()
- Usa import math para math.pi
"""

import math


# ============================================================
# Clase padre: Figura
# ============================================================

class Figura:
    def __init__(self, color):
        # TODO: Guardar color como atributo
        pass

    def calcular_area(self):
        # TODO: Retornar 0 (este es el método base)
        pass

    def describir(self):
        # TODO: Imprimir "Soy una figura de color [color]"
        pass


# ============================================================
# Clase hija: Rectangulo
# Hereda de Figura y agrega: ancho, alto
# ============================================================

class Rectangulo:  # TODO: Agregar la herencia de Figura
    def __init__(self, color, ancho, alto):
        # TODO: Llamar al __init__ del padre con super()
        # TODO: Guardar ancho y alto como atributos propios
        pass

    def calcular_area(self):
        # TODO: Retornar ancho * alto
        pass

    def describir(self):
        # TODO: Llamar a super().describir() primero
        # TODO: Imprimir "Soy un rectángulo de [ancho]x[alto]"
        # TODO: Imprimir "Mi área es [calcular_area()]"
        pass


# ============================================================
# Clase hija: Circulo
# Hereda de Figura y agrega: radio
# ============================================================

class Circulo:  # TODO: Agregar la herencia de Figura
    def __init__(self, color, radio):
        # TODO: Llamar al __init__ del padre con super()
        # TODO: Guardar radio como atributo propio
        pass

    def calcular_area(self):
        # TODO: Retornar math.pi * radio ** 2
        pass

    def describir(self):
        # TODO: Llamar a super().describir() primero
        # TODO: Imprimir "Soy un círculo de radio [radio]"
        # TODO: Imprimir "Mi área es [calcular_area():.2f]"
        pass


# ============================================================
# Pruebas — NO modificar esta sección
# Si tu código es correcto, esto debería funcionar sin errores
# ============================================================

if __name__ == "__main__":

    print("Probando Rectángulo...")
    rect = Rectangulo("azul", 10, 5)
    rect.describir()
    # Esperado:
    #   Soy una figura de color azul
    #   Soy un rectángulo de 10x5
    #   Mi área es 50

    print()

    print("Probando Círculo...")
    circ = Circulo("rojo", 7)
    circ.describir()
    # Esperado:
    #   Soy una figura de color rojo
    #   Soy un círculo de radio 7
    #   Mi área es 153.94

    print()

    print("Verificando herencia...")
    print(f"Rectangulo es Figura: {isinstance(rect, Figura)}")  # True
    print(f"Circulo es Figura: {isinstance(circ, Figura)}")     # True

    print()
    print(f"Área rectángulo: {rect.calcular_area()}")     # 50
    print(f"Área círculo: {circ.calcular_area():.2f}")    # 153.94
