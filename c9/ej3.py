def sumar_todos(*numeros):

    print(f"Recibido: {numeros}")

    print(f"Tipo: {type(numeros)}")


    total = 0

    for num in numeros:

        total += num

    return total


# Probemos con diferentes cantidades

print("Suma de 1, 2:", sumar_todos(1, 2))

print("Suma de 1-5:", sumar_todos(1, 2, 3, 4, 5))

print("Suma de solo 10:", sumar_todos(10))

print("Suma de nada:", sumar_todos())