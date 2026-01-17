# Ejercicio 4

try:
    edad = int(input("Ingresa tu edad: "))

    if edad < 0:
        print("Edad no válida")
    elif edad < 13:
        print("Eres un niño")
    elif edad < 18:
        print("Eres un adolescente")
    elif edad < 65:
        print("Eres un adulto")
    else:
        print("Eres un adulto mayor")

except ValueError:
    print("Error: debes ingresar un número entero")

