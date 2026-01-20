# password.py
password_correcto = "python123"

while True:
    intento = input("Password: ")
    
    if intento == password_correcto:
        print("Acceso concedido!")
        break
    else:
        print("Incorrecta, intenta de nuevo")

