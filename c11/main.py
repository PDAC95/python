# main.py
# Programa principal - Menú interactivo del sistema de tareas

# "Importar TODAS las funciones que creamos en tareas.py"
from tareas import (
    agregar_tarea,
    buscar_tareas,
    marcar_completada,
    total_por_prioridad,
    porcentaje_completadas,
    tareas_por_categoria,
    generar_reporte,
    tareas_urgentes
)

# "Importar los datos de prueba para no empezar vacíos"
from datos_prueba import tareas_ejemplo


def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n" + "="*50)
    print("   SISTEMA DE GESTIÓN DE TAREAS")
    print("="*50)
    print("1. Ver todas las tareas")
    print("2. Agregar nueva tarea")
    print("3. Marcar tarea como completada")
    print("4. Buscar tareas (filtros)")
    print("5. Ver estadísticas")
    print("6. Generar reporte")
    print("7. Ver tareas urgentes")
    print("0. Salir")
    print("="*50)


def main():
    """Función principal del programa."""
    
    # "Crear copia de los datos de prueba"
    # "IMPORTANTE: .copy() para no modificar el original"
    tareas = tareas_ejemplo.copy()
    
    print("\n¡Bienvenido al Sistema de Gestión de Tareas!")
    
    # "Loop infinito - solo salimos con break cuando eligen 0"
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione opción: ")
        
        # OPCIÓN 0: SALIR
        if opcion == "0":
            print("\n¡Hasta luego!")
            break
        
        # OPCIÓN 1: VER TODAS LAS TAREAS
        elif opcion == "1":
            print("\n📋 TODAS LAS TAREAS:")
            print("-" * 50)
            
            if not tareas:
                print("No hay tareas registradas")
            else:
                for t in tareas:
                    # "Operador ternario para el emoji"
                    estado = "✓" if t["completada"] else "○"
                    print(f"{estado} [{t['id']}] {t['titulo']} - {t['prioridad']}")
        
        # OPCIÓN 2: AGREGAR NUEVA TAREA
        elif opcion == "2":
            print("\n➕ AGREGAR NUEVA TAREA:")
            
            titulo = input("Título: ")
            descripcion = input("Descripción (Enter para omitir): ")
            prioridad = input("Prioridad (alta/media/baja, Enter=media): ") or "media"
            categoria = input("Categoría (Enter=general): ") or "general"
            
            # "Llamar nuestra función agregar_tarea()"
            nueva = agregar_tarea(tareas, titulo, descripcion, prioridad, categoria)
            print(f"\n✓ Tarea '{nueva['titulo']}' creada con ID {nueva['id']}")
        
        # OPCIÓN 3: MARCAR COMO COMPLETADA
        elif opcion == "3":
            print("\n✓ MARCAR TAREA COMO COMPLETADA:")
            try:
                tarea_id = int(input("ID de la tarea: "))
                
                if marcar_completada(tareas, tarea_id):
                    print("✓ Tarea marcada como completada")
                else:
                    print("✗ No se encontró tarea con ese ID")
            except ValueError:
                print("✗ Error: ingrese un número válido")
        
        # OPCIÓN 4: BUSCAR CON FILTROS
        elif opcion == "4":
            print("\n🔍 BUSCAR TAREAS:")
            print("1. Por prioridad")
            print("2. Por categoría")
            print("3. Solo pendientes")
            
            filtro = input("Seleccione: ")
            
            if filtro == "1":
                prio = input("Prioridad (alta/media/baja): ")
                resultados = buscar_tareas(tareas, prioridad=prio)
            elif filtro == "2":
                cat = input("Categoría: ")
                resultados = buscar_tareas(tareas, categoria=cat)
            elif filtro == "3":
                resultados = buscar_tareas(tareas, completada=False)
            else:
                resultados = []
            
            print(f"\nSe encontraron {len(resultados)} tareas:")
            for t in resultados:
                estado = "✓" if t["completada"] else "○"
                print(f"{estado} {t['titulo']} - {t['categoria']}")
        
        # OPCIÓN 5: ESTADÍSTICAS
        elif opcion == "5":
            print("\n📊 ESTADÍSTICAS:")
            print("-" * 50)
            
            conteo = total_por_prioridad(tareas)
            print(f"Alta prioridad: {conteo['alta']}")
            print(f"Media prioridad: {conteo['media']}")
            print(f"Baja prioridad: {conteo['baja']}")
            print(f"\nCompletadas: {porcentaje_completadas(tareas)}%")
            
            print("\nPor categoría:")
            agrupadas = tareas_por_categoria(tareas)
            for cat, lista in agrupadas.items():
                print(f"  {cat}: {len(lista)} tareas")
        
        # OPCIÓN 6: GENERAR REPORTE
        elif opcion == "6":
            print("\n📄 REPORTE:")
            print("-" * 50)
            
            reporte = generar_reporte(tareas, mostrar_prioridad=True)
            print(reporte)
        
        # OPCIÓN 7: TAREAS URGENTES
        elif opcion == "7":
            print("\n⚠️  TAREAS URGENTES:")
            print("-" * 50)
            
            urgentes = tareas_urgentes(tareas)
            
            if urgentes:
                for linea in urgentes:
                    print(linea)
            else:
                print("✓ No hay tareas urgentes pendientes")
        
        # OPCIÓN INVÁLIDA
        else:
            print("\n✗ Opción inválida. Intente de nuevo.")


# "Patrón estándar en Python"
# "Solo ejecuta main() si este es el archivo principal"
if __name__ == "__main__":
    main()