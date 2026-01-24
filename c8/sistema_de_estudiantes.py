
def agregar_estudiante(nombre, calificaciones):
    """Función para crear un estudiante con su promedio y estatus"""
    # Calcula el promedio sumando las calificaciones y dividiéndolas entre cuántas hay
    promedio = sum(calificaciones) / len(calificaciones)
    
    # Decide si está aprobado o reprobado según el promedio
    status = "Aprobado" if promedio >= 70 else "Reprobado"
    
    # Regresa un diccionario con toda la info del estudiante
    return {
        "nombre": nombre,
        "promedio": promedio,
        "status": status
    }

# Función que filtra solo a los estudiantes aprobados
def obtener_aprobados(lista_estudiantes):
    aprobados = []  # Lista vacía para guardar aprobados
    
    # Recorremos todos los estudiantes
    for estudiante in lista_estudiantes:
        # Si el promedio es 70 o más, lo agregamos a la lista
        if estudiante["promedio"] >= 70:
            aprobados.append(estudiante)
    
    # Regresamos la lista de aprobados
    return aprobados

# Función para calcular estadísticas generales
def mostrar_estadisticas(lista_estudiantes):
    # Sacamos solo los promedios de cada estudiante
    promedios = [e["promedio"] for e in lista_estudiantes]
    
    # Calculamos el promedio general del grupo
    promedio_general = sum(promedios) / len(promedios)

    # Buscamos al estudiante con el promedio más alto
    mejor = max(lista_estudiantes, key=lambda e: e["promedio"])
    
    # Buscamos al estudiante con el promedio más bajo
    peor = min(lista_estudiantes, key=lambda e: e["promedio"])

    # Regresamos las estadísticas en un diccionario
    return {
        "promedio_general": promedio_general,
        "mejor_estudiante": mejor["nombre"],
        "peor_estudiante": peor["nombre"]
    }

# ---------------- PROGRAMA PRINCIPAL ----------------

estudiantes = []  # Lista donde guardaremos a todos los estudiantes

# Agregamos estudiantes usando la función
estudiantes.append(agregar_estudiante("Ana", [85, 90, 78]))
estudiantes.append(agregar_estudiante("Carlos", [60, 55, 60]))
estudiantes.append(agregar_estudiante("Maria", [95, 92, 88]))

# Mostramos todos los estudiantes
print("Todos los estudiantes:")
for e in estudiantes:
    print(f"  {e['nombre']}: {e['promedio']:.1f} - {e['status']}")

# Mostramos solo los aprobados
print("\nAprobados:")
for e in obtener_aprobados(estudiantes):
    print(f"  {e['nombre']}")

# Mostramos estadísticas del grupo
print("\nEstadisticas:")
stats = mostrar_estadisticas(estudiantes)
print(f"  Promedio general: {stats['promedio_general']:.1f}")
print(f"  Mejor: {stats['mejor_estudiante']}")
print(f"  Peor: {stats['peor_estudiante']}")
