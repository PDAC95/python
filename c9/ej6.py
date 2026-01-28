def crear_usuario(nombre, **datos_extra):

    print(f"Nombre: {nombre}")

    print(f"Datos extra: {datos_extra}")

    print(f"Tipo: {type(datos_extra)}")


    # Crear diccionario base

    usuario = {"nombre": nombre}


    # Agregar datos extra

    for clave, valor in datos_extra.items():

        usuario[clave] = valor


    return usuario


# Pruebas

print("=== Usuario 1 ===")

u1 = crear_usuario("Ana", edad=25, ciudad="Madrid")

print(f"Resultado: {u1}")


print("\n=== Usuario 2 ===")

u2 = crear_usuario("Carlos",

                   profesion="Developer",

                   experiencia=5,

                   remoto=True,

                   skills=["Python", "JavaScript"])

print(f"Resultado: {u2}")


print("\n=== Usuario 3 ===")

u3 = crear_usuario("Luis")  # Sin datos extra

print(f"Resultado: {u3}")