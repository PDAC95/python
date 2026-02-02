from math import pi

radios = [1, 2, 3, 4, 5, 10, 20]

# area = []

# for radio in radios:
#     area = pi * radio **2
#     areas.append(area)

def calcular_area(radio):
    return pi * radio **2

resultado = map(calcular_area, radios)
print('con map():', resultado)

areas = list(resultado)
print('con map():', areas)

#map(funcion, iterable)
#funcion se va a aplicar a cada elemento
#lista
