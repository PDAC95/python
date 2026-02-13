def calculadora():

    while True:

        print("\n--- CALCULADORA ---")

        print("(Escribe 'salir' para terminar)\n")


        entrada = input("Primer número: ")

        if entrada.lower() == "salir":

            print("¡Hasta luego!")

            break


        try:

            a = float(entrada)

            b = float(input("Segundo número: "))

        except ValueError:

            print("❌ Debes escribir números válidos")

            continue


        operacion = input("Operación (+, -, *, /): ")


        try:

            if operacion == "+":

                resultado = a + b

            elif operacion == "-":

                resultado = a - b

            elif operacion == "*":

                resultado = a * b

            elif operacion == "/":

                resultado = a / b

            else:

                print("❌ Operación no válida")

                continue


            print(f"✅ Resultado: {resultado}")


        except ZeroDivisionError:

            print("❌ No puedes dividir entre cero")


calculadora()