# tareas.py
# Sistema de Gestión de Tareas - Clase 11

from datetime import date


def agregar_tarea(tareas, titulo, descripcion="", prioridad="media", categoria="general"):
    """
    Agrega una nueva tarea a la lista.
    
    Args:
        tareas: Lista de tareas existentes
        titulo: Nombre de la tarea (requerido)
        descripcion: Detalles adicionales (opcional)
        prioridad: "alta", "media" o "baja" (default: "media")
        categoria: Categoría de la tarea (default: "general")
    
    Returns:
        dict: La tarea creada
    """
    if prioridad not in ["alta", "media", "baja"]:
        prioridad = "media"
    
    nuevo_id = max([t["id"] for t in tareas], default=0) + 1
    
    nueva_tarea = {
        "id": nuevo_id,
        "titulo": titulo,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "categoria": categoria,
        "completada": False,
        "fecha_creacion": str(date.today())
    }
    
    tareas.append(nueva_tarea)
    return nueva_tarea


def buscar_tareas(tareas, **filtros):
    """
    Busca tareas que coincidan con los filtros dados.
    
    Args:
        tareas: Lista de tareas
        **filtros: Criterios de búsqueda (prioridad, categoria, completada)
    
    Returns:
        list: Tareas que cumplen TODOS los filtros
    """
    resultado = tareas
    
    if "prioridad" in filtros:
        resultado = list(filter(
            lambda t: t["prioridad"] == filtros["prioridad"],
            resultado
        ))
    
    if "categoria" in filtros:
        resultado = list(filter(
            lambda t: t["categoria"] == filtros["categoria"],
            resultado
        ))
    
    if "completada" in filtros:
        resultado = list(filter(
            lambda t: t["completada"] == filtros["completada"],
            resultado
        ))
    
    return resultado


def marcar_completada(tareas, tarea_id):
    """
    Marca una tarea como completada.
    
    Args:
        tareas: Lista de tareas
        tarea_id: ID de la tarea a completar
    
    Returns:
        bool: True si se encontró y marcó, False si no existe
    """
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            return True
    
    return False


def total_por_prioridad(tareas):
    """
    Cuenta tareas por nivel de prioridad.
    
    Args:
        tareas: Lista de tareas
    
    Returns:
        dict: {"alta": n, "media": n, "baja": n}
    """
    return {
        "alta": len(list(filter(lambda t: t["prioridad"] == "alta", tareas))),
        "media": len(list(filter(lambda t: t["prioridad"] == "media", tareas))),
        "baja": len(list(filter(lambda t: t["prioridad"] == "baja", tareas)))
    }


def porcentaje_completadas(tareas):
    """
    Calcula el porcentaje de tareas completadas.
    
    Args:
        tareas: Lista de tareas
    
    Returns:
        float: Porcentaje con 1 decimal
    """
    if not tareas:
        return 0
    
    completadas = len(list(filter(lambda t: t["completada"], tareas)))
    return round(completadas / len(tareas) * 100, 1)


def tareas_por_categoria(tareas):
    """
    Agrupa tareas por categoría.
    
    Args:
        tareas: Lista de tareas
    
    Returns:
        dict: {categoria: [lista de tareas]}
    """
    categorias = set(map(lambda t: t["categoria"], tareas))
    
    return {
        cat: list(filter(lambda t: t["categoria"] == cat, tareas))
        for cat in categorias
    }


def generar_reporte(tareas, *categorias, formato="texto", **opciones):
    """
    Genera un reporte personalizado de tareas.
    
    Args:
        tareas: Lista de tareas
        *categorias: Categorías a incluir (si vacío, incluye todas)
        formato: "texto" o "lista" (default: "texto")
        **opciones: incluir_completadas (bool), mostrar_prioridad (bool)
    
    Returns:
        str o list: Reporte en el formato especificado
    """
    if categorias:
        tareas_filtradas = list(filter(
            lambda t: t["categoria"] in categorias,
            tareas
        ))
    else:
        tareas_filtradas = tareas
    
    if not opciones.get("incluir_completadas", True):
        tareas_filtradas = list(filter(
            lambda t: not t["completada"],
            tareas_filtradas
        ))
    
    if formato == "lista":
        return [t["titulo"] for t in tareas_filtradas]
    else:
        lineas = []
        
        for tarea in tareas_filtradas:
            linea = f"- {tarea['titulo']}"
            
            if opciones.get("mostrar_prioridad", False):
                linea += f" [{tarea['prioridad']}]"
            
            lineas.append(linea)
        
        return "\n".join(lineas)


def tareas_urgentes(tareas, dias=7):
    """
    Obtiene tareas urgentes formateadas.
    
    Args:
        tareas: Lista de tareas
        dias: Para mejora futura (no usado aún)
    
    Returns:
        list: Lista de strings con tareas urgentes formateadas
    """
    urgentes = list(filter(
        lambda t: t["prioridad"] == "alta" and not t["completada"],
        tareas
    ))
    
    formateadas = list(map(
        lambda t: f"⚠️ [URGENTE] {t['titulo']} - Categoría: {t['categoria']}",
        urgentes
    ))
    
    return formateadas