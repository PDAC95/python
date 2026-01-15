#password 

password = input("dime un password: ")

#verificar
longitud_ok= len(password) >= 8
no_password = password != "password"
no_num = password != "12345678"

password_valido = longitud_ok and no_password and no_num

print(f"Password valida: {password_valido}")

