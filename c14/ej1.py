# try:

#     numero = int(input("Escribe un número: "))

#     print(f"El doble es: {numero * 2}")

# except ValueError:

#     print("❌ Eso no es un número válido")


intentos = 3

while intentos > 0:
    try:
        numero = int(input('dame un numero:'))
        break
    except ValueError:
        intentos -= 1
        print (f'x invalido, te quedan {intentos} intentos')
else:
    print('se acabaron los intentos')
    numero = 0 #valor por defecto