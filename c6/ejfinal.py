historial = ""
# Aquí vamos a guardar todas las operaciones que el usuario haga

print("=== CALCULADORA ===")


while True:
    # Este while hace que el programa se repita
    # Solo se va a detener cuando el usuario elija "Salir"

    print("\n1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Historial 6.Salir")
    # Menú con las opciones disponibles

    op = input("Opcion: ")
    # Le pedimos al usuario que elija una opción

    if op == "1":  # SUMAR
        n = int(input("Cuantos numeros? "))
        # Preguntamos cuántos números se van a sumar

        suma = 0
        # Variable donde iremos acumulando la suma

        for i in range(1, n + 1):
            # El for se repite la cantidad de números indicada

            num = float(input(f"Numero {i}: "))
            # Pedimos cada número

            suma += num
            # Sumamos el número al total

        print(f"Resultado: {suma}")
        # Mostramos el resultado

        historial += f"Suma: {suma}\n"
        # Guardamos la operación en el historial

    elif op == "2":  # RESTAR
        a, b = float(input("Num 1: ")), float(input("Num 2: "))
        # Pedimos dos números

        res = a - b
        # Restamos el segundo al primero

        print(f"Resultado: {res}")
        # Mostramos el resultado

        historial += f"{a}-{b}={res}\n"
        # Guardamos la operación

    elif op == "3":  # MULTIPLICAR
        a, b = float(input("Num 1: ")), float(input("Num 2: "))
        # Pedimos dos números

        res = a * b
        # Multiplicamos los números

        print(f"Resultado: {res}")
        # Mostramos el resultado

        historial += f"{a}*{b}={res}\n"
        # Guardamos la operación

    elif op == "4":  # DIVIDIR
        a, b = float(input("Dividendo: ")), float(input("Divisor: "))
        # Pedimos los valores para dividir

        if b == 0:
            # Si el divisor es cero, no se puede dividir
            print("Error: division por cero!")
        else:
            res = a / b
            # Hacemos la división

            print(f"Resultado: {res}")
            # Mostramos el resultado

            historial += f"{a}/{b}={res}\n"
            # Guardamos la operación

    elif op == "5":
        # Mostramos el historial de operaciones
        print("\n=== HISTORIAL ===\n" + (historial if historial else "Vacio"))

    elif op == "6":
        # Opción para salir del programa
        print("Adios!")
        break
        # break corta el while y termina el programa

    else:
        # Si la opción no existe
        print("Opcion invalida")
