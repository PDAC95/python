# ============================================
# EJERCICIO 1: Validar datos de tarea
# ============================================
# Crea una función crear_tarea(titulo, prioridad, categoria)
# que valide los datos usando raise ValueError
#
# Validaciones:
# - titulo: string no vacío
# - prioridad: debe ser "alta", "media" o "baja"
# - categoria: string no vacío
#
# Si es válido, retorna dict con los datos
# Si no es válido, lanza ValueError con mensaje claro

def crear_tarea(titulo, prioridad, categoria):
    """
    Crea una tarea con validaciones.

    Args:
        titulo: Titulo de la tarea (string no vacio)
        prioridad: 'alta', 'media' o 'baja'
        categoria: Categoria de la tarea (string no vacio)

    Returns:
        Diccionario con los datos de la tarea

    Raises:
        ValueError: Si algun dato es invalido
    """
    # Validar titulo
    if not isinstance(titulo, str) or len(titulo.strip()) == 0:
        raise ValueError("El titulo no puede estar vacio")

    # Validar prioridad
    prioridades_validas = ["alta", "media", "baja"]
    if prioridad not in prioridades_validas:
        raise ValueError(f"Prioridad debe ser una de: {prioridades_validas}")

    # Validar categoria
    if not isinstance(categoria, str) or len(categoria.strip()) == 0:
        raise ValueError("La categoria no puede estar vacia")

    # Crear y retornar tarea
    return {
        "titulo": titulo.strip(),
        "prioridad": prioridad,
        "categoria": categoria.strip(),
        "completada": False
    }


# Pruebas (descomenta para probar)
print(crear_tarea("Estudiar", "alta", "estudio"))
print(crear_tarea("", "alta", "estudio"))  # Debe lanzar error
print(crear_tarea("Estudiar", "urgente", "estudio"))  # Debe lanzar error
