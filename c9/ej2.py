def crear_perfil(nombre, edad, ciudad="Desconocida", activo=True):

    """

    Crea un perfil de usuario con valores opcionales.


    Args:

        nombre: Nombre del usuario (requerido)

        edad: Edad del usuario (requerido)

        ciudad: Ciudad del usuario (default: "Desconocida")

        activo: Si el usuario está activo (default: True)


    Returns:

        dict: Diccionario con el perfil del usuario

    """

    return {

        "nombre": nombre,

        "edad": edad,

        "ciudad": ciudad,

        "activo": activo

    }


# Pruebas

perfil1 = crear_perfil("Ana", 25)

print(perfil1)

# {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Desconocida', 'activo': True}


perfil2 = crear_perfil("Carlos", 30, "Madrid")

print(perfil2)

# {'nombre': 'Carlos', 'edad': 30, 'ciudad': 'Madrid', 'activo': True}


perfil3 = crear_perfil("Elena", 28, "Barcelona", False)

print(perfil3)

# {'nombre': 'Elena', 'edad': 28, 'ciudad': 'Barcelona', 'activo': False}


# También podemos usar argumentos por nombre

perfil4 = crear_perfil("Luis", 35, activo=False)

print(perfil4)

# {'nombre': 'Luis', 'edad': 35, 'ciudad': 'Desconocida', 'activo': False}