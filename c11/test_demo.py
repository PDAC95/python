# test_demo.py
# Script para demos rápidas durante la clase

from tareas import *
from datos_prueba import tareas_ejemplo

# "Crear copia para no modificar original"
tareas = tareas_ejemplo.copy()

print("=" * 50)
print("DEMO RÁPIDA DEL SISTEMA")
print("=" * 50)

# Demo 1: Agregar tarea
print("\n1. Agregar tarea:")
nueva = agregar_tarea(tareas, "Demo tarea", prioridad="alta", categoria="test")
print(f"✓ Creada: {nueva['titulo']} con ID {nueva['id']}")

# Demo 2: Buscar
print("\n2. Buscar alta prioridad:")
altas = buscar_tareas(tareas, prioridad="alta")
print(f"Encontradas: {len(altas)} tareas")

# Demo 3: Estadísticas
print("\n3. Estadísticas:")
print(total_por_prioridad(tareas))
print(f"Completadas: {porcentaje_completadas(tareas)}%")

# Demo 4: Reporte
print("\n4. Reporte:")
print(generar_reporte(tareas, "trabajo", mostrar_prioridad=True))

print("\n" + "=" * 50)


# # ✅ CHECKLIST FINAL PRE-CLASE:
# □ Carpeta proyecto_tareas/ creada
# □ tareas.py completo (8 funciones con comentarios)
# □ datos_prueba.py completo (7 tareas de ejemplo)
# □ main.py completo (menú con 7 opciones)
# □ test_demo.py (opcional)
# □ Python funcionando en tu máquina
# □ VS Code abierto
# □ Terminal funcionando
# □ Slides listos
# □ Has probado ejecutar: python main.py
# □ Todo funciona correctamente