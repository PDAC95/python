# Paso 1: Importar pi del módulo math

from math import pi

# Paso 2: Crear la función lambda

area_circulo = lambda r: pi * r ** 2

# Paso 3: Probar con diferentes radios

print(f"Radio 1: {area_circulo(1):.2f}")      
print(f"Radio 2.5: {area_circulo(2.5):.2f}")  
print(f"Radio 5: {area_circulo(5):.2f}")      
print(f"Radio 10: {area_circulo(10):.2f}")    