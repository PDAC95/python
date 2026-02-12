# ============================================
# Ejemplo: Excepciones personalizadas
# ============================================
# Sistema de excepciones para el proyecto de tareas

class TareaError(Exception):
    """Error base para el sistema de tareas."""
    pass


class TituloVacioError(TareaError):
    """El titulo de la tarea esta vacio."""
    pass


class PrioridadInvalidaError(TareaError):
    """La prioridad no es valida."""
    pass


class CategoriaVaciaError(TareaError):
    """La categoria esta vacia."""
    pass


def crear_tarea_con_excepciones_propias(titulo, prioridad, categoria):
    """Crea una tarea usando excepciones personalizadas."""

    if not titulo or len(titulo.strip()) == 0:
        raise TituloVacioError("El titulo no puede estar vacio")

    if prioridad not in ["alta", "media", "baja"]:
        raise PrioridadInvalidaError(f"'{prioridad}' no es una prioridad valida")

    if not categoria or len(categoria.strip()) == 0:
        raise CategoriaVaciaError("La categoria no puede estar vacia")

    return {
        "titulo": titulo.strip(),
        "prioridad": prioridad,
        "categoria": categoria.strip(),
        "completada": False
    }


# Demostracion de uso
if __name__ == "__main__":
    # Manejo especifico por tipo de error
    def menu_crear_tarea():
        titulo = input("Titulo: ")
        prioridad = input("Prioridad (alta/media/baja): ")
        categoria = input("Categoria: ")

        try:
            tarea = crear_tarea_con_excepciones_propias(titulo, prioridad, categoria)
            print(f"Tarea creada: {tarea}")
        except TituloVacioError:
            print("Error: Debes escribir un titulo")
        except PrioridadInvalidaError as e:
            print(f"Error: {e}")
        except CategoriaVaciaError:
            print("Error: Debes escribir una categoria")
        except TareaError:
            print("Error desconocido en la tarea")

    menu_crear_tarea()
