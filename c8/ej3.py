def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir por cero"
    return a / b

def menu():
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

# Programa principal
while True:
    menu()
    opcion = input("Elige opcion: ")

    if opcion == "5":
        print("Adios!")
        break

    num1 = float(input("Primer numero: "))
    num2 = float(input("Segundo numero: "))

    if opcion == "1":
        resultado = sumar(num1, num2)
    elif opcion == "2":
        resultado = restar(num1, num2)
    elif opcion == "3":
        resultado = multiplicar(num1, num2)
    elif opcion == "4":
        resultado = dividir(num1, num2)
    else:
        print("Opcion invalida")
        continue

    print(f"Resultado: {resultado}")