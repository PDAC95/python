#si funcione

def crear_usuario(nombre, email, activo=True, rol="usuario"):

    return {

        "nombre": nombre,

        "email": email,

        "activo": activo,

        "rol": rol

    }


# Múltiples formas de llamar:

u1 = crear_usuario("Ana", "ana@mail.com")  # usa defaults

u2 = crear_usuario("Carlos", "carlos@mail.com", False)  # activo=False

u3 = crear_usuario("Luis", "luis@mail.com", True, "admin")  # especifica todo

u4 = crear_usuario("María", "maria@mail.com", rol="moderador")  # solo cambia rol


print(u1)

print(u2)

print(u3)

print(u4)