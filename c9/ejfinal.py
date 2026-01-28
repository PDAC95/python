# Lista global para almacenar eventos (simulación de base de datos)

EVENTOS_DB = []



def registrar_evento(nombre, fecha, *participantes, **detalles):

    """

    Registra un nuevo evento con participantes y detalles opcionales.


    Args:

        nombre: Nombre del evento (requerido)

        fecha: Fecha del evento (requerido)

        *participantes: Lista variable de nombres de participantes

        **detalles: Detalles adicionales (ubicacion, tipo, capacidad, etc.)


    Returns:

        dict: Diccionario con toda la información del evento

    """

    evento = {

        "nombre": nombre,

        "fecha": fecha,

        "participantes": list(participantes),

        "num_participantes": len(participantes)

    }


    # Agregar todos los detalles

    for clave, valor in detalles.items():

        evento[clave] = valor


    # Guardar en "base de datos"

    EVENTOS_DB.append(evento)


    return evento



def buscar_eventos_por(**filtros):

    """

    Busca eventos que coincidan con los filtros dados.


    Args:

        **filtros: Criterios de búsqueda (ubicacion="Madrid", tipo="tech", etc.)


    Returns:

        list: Lista de eventos que coinciden con TODOS los filtros

    """

    resultados = []


    for evento in EVENTOS_DB:

        coincide = True

        for clave, valor in filtros.items():

            if clave not in evento or evento[clave] != valor:

                coincide = False

                break


        if coincide:

            resultados.append(evento)


    return resultados



def generar_reporte(*eventos):

    """

    Genera estadísticas de los eventos dados.


    Args:

        *eventos: Eventos a incluir en el reporte


    Returns:

        dict: Estadísticas calculadas

    """

    if not eventos:

        return {"error": "No hay eventos para reportar"}


    total_participantes = 0

    ubicaciones = set()


    for evento in eventos:

        total_participantes += evento.get("num_participantes", 0)

        if "ubicacion" in evento:

            ubicaciones.add(evento["ubicacion"])


    return {

        "total_eventos": len(eventos),

        "total_participantes": total_participantes,

        "promedio_participantes": total_participantes / len(eventos),

        "ubicaciones_unicas": list(ubicaciones),

        "num_ubicaciones": len(ubicaciones)

    }



# ===== PROGRAMA PRINCIPAL =====

if __name__ == "__main__":

    # Registrar eventos

    print("=== Registrando eventos ===")


    evento1 = registrar_evento(

        "Python Meetup", "2024-03-15",

        "Ana", "Carlos", "Luis", "María", "Pedro",

        ubicacion="Madrid",

        tipo="tech",

        capacidad=50

    )

    print(f"Evento 1: {evento1}")


    evento2 = registrar_evento(

        "Data Science Workshop", "2024-03-20",

        "Julia", "Roberto",

        ubicacion="Barcelona",

        tipo="tech",

        duracion="4 horas"

    )

    print(f"Evento 2: {evento2}")


    evento3 = registrar_evento(

        "Networking Café", "2024-03-25",

        "Lucía", "Miguel", "Sara",

        ubicacion="Madrid",

        tipo="social"

    )

    print(f"Evento 3: {evento3}")


    # Buscar eventos

    print("\n=== Buscando eventos ===")


    eventos_tech = buscar_eventos_por(tipo="tech")

    print(f"Eventos tech: {len(eventos_tech)} encontrados")


    eventos_madrid = buscar_eventos_por(ubicacion="Madrid")

    print(f"Eventos en Madrid: {len(eventos_madrid)} encontrados")


    # Generar reporte

    print("\n=== Generando reporte ===")


    reporte_todos = generar_reporte(evento1, evento2, evento3)

    print(f"Reporte de todos los eventos:")

    for clave, valor in reporte_todos.items():

        print(f"  {clave}: {valor}")


    reporte_tech = generar_reporte(*eventos_tech)

    print(f"\nReporte de eventos tech:")

    for clave, valor in reporte_tech.items():

        print(f"  {clave}: {valor}")