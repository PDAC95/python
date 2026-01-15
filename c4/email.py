#email

email = input("Email: ")

# Verificar @
tiene_arroba = email.count("@") == 1
# o: tiene_arroba = email.find("@") != -1

# Verificar extension
extension_valida = (email.endswith(".com") or
                   email.endswith(".org") or
                   email.endswith(".net") or
                   email.endswith(".edu"))

print(f"\nTiene @: {'Si' if tiene_arroba else 'No'}")
print(f"Extension valida: {'Si' if extension_valida else 'No'}")
print(f"En minusculas: {email.lower()}")


