from tareas import (
    agregar_tarea,
    buscar_tareas,
    marcar_completada,
    total_por_prioridad,
    porcentaje_completadas,
    tareas_por_categoria,
    generar_reporte,
    tareas_urgentes,
    guardar_tareas,
    cargar_tareas
)


def mostrar_menu():
    print("\n" + "="*50)
    print("SISTEMA DE GESTIÓN DE TAREAS")
    print("="*50)
    print("1. Ver todas las tareas")
    print("2. Agregar nueva tarea")
    print("3. Marcar tarea como completada")
    print("4. Buscar tareas")
    print("5. Ver estadísticas")
    print("6. Generar reporte completo")
    print("7. Ver tareas urgentes")
    print("0. Salir")
    print("="*50)


def main():
    archivo = "tareas.json"
    tareas = cargar_tareas(archivo)
    
    if not tareas:
        print("Primera vez - cargando datos de ejemplo...")
        from datos_prueba import tareas_ejemplo
        tareas = tareas_ejemplo.copy()
        guardar_tareas(tareas, archivo)
    
    print(f"\n{'='*50}")
    print(f"Bienvenido! Tienes {len(tareas)} tareas guardadas.")
    print(f"{'='*50}\n")
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione opción: ").strip()
        
        if opcion == "0":
            guardar_tareas(tareas, archivo)
            print("\n✓ Tareas guardadas!")
            print("Hasta luego.\n")
            break
        
        elif opcion == "1":
            print(f"\n{'='*50}")
            print("TODAS LAS TAREAS")
            print(f"{'='*50}")
            if not tareas:
                print("No hay tareas.")
            else:
                for tarea in tareas:
                    completada = "✓" if tarea["completada"] else "✗"
                    print(f"[{completada}] {tarea['id']}. {tarea['titulo']} "
                          f"({tarea['prioridad']}) - {tarea['categoria']}")
            print()
        
        elif opcion == "2":
            print(f"\n{'='*50}")
            print("AGREGAR NUEVA TAREA")
            print(f"{'='*50}")
            
            titulo = input("Título: ").strip()
            prioridad = input("Prioridad (alta/media/baja): ").strip().lower()
            categoria = input("Categoría: ").strip()
            
            nueva_tarea = agregar_tarea(tareas, titulo, prioridad, categoria)
            
            if nueva_tarea:
                print(f"\n✓ Tarea '{titulo}' agregada con ID {nueva_tarea['id']}")
                guardar_tareas(tareas, archivo)
            else:
                print("\n✗ Error al agregar tarea")
            print()
        
        elif opcion == "3":
            print(f"\n{'='*50}")
            print("MARCAR TAREA COMO COMPLETADA")
            print(f"{'='*50}")
            
            try:
                id_tarea = int(input("ID de la tarea: ").strip())
                
                if marcar_completada(tareas, id_tarea):
                    print(f"\n✓ Tarea {id_tarea} marcada como completada")
                    guardar_tareas(tareas, archivo)
                else:
                    print(f"\n✗ No se encontró tarea con ID {id_tarea}")
            except ValueError:
                print("\n✗ ID inválido. Debe ser un número.")
            print()
        
        elif opcion == "4":
            print(f"\n{'='*50}")
            print("BUSCAR TAREAS")
            print(f"{'='*50}")
            
            palabra = input("Palabra a buscar: ").strip()
            resultados = buscar_tareas(tareas, palabra)
            
            if resultados:
                print(f"\n✓ Se encontraron {len(resultados)} tareas:")
                for tarea in resultados:
                    print(f"  - {tarea['id']}. {tarea['titulo']}")
            else:
                print(f"\n✗ No se encontraron tareas con '{palabra}'")
            print()
        
        elif opcion == "5":
            print(f"\n{'='*50}")
            print("ESTADÍSTICAS")
            print(f"{'='*50}")
            
            totales = total_por_prioridad(tareas)
            print("\nTareas por prioridad:")
            for prioridad, cantidad in totales.items():
                print(f"  {prioridad}: {cantidad}")
            
            porcentaje = porcentaje_completadas(tareas)
            print(f"\nCompletadas: {porcentaje:.1f}%")
            
            por_cat = tareas_por_categoria(tareas)
            print("\nTareas por categoría:")
            for cat, cantidad in por_cat.items():
                print(f"  {cat}: {cantidad}")
            print()
        
        elif opcion == "6":
            print(f"\n{'='*50}")
            print("REPORTE COMPLETO")
            print(f"{'='*50}\n")
            
            reporte = generar_reporte(tareas)
            print(reporte)
        
        elif opcion == "7":
            print(f"\n{'='*50}")
            print("TAREAS URGENTES")
            print(f"{'='*50}")
            
            urgentes = tareas_urgentes(tareas)
            if urgentes:
                print(f"\n✓ Tienes {len(urgentes)} tareas urgentes:")
                for tarea in urgentes:
                    print(f"  - {tarea['id']}. {tarea['titulo']} ({tarea['categoria']})")
            else:
                print("\n✓ No tienes tareas urgentes")
            print()
        
        else:
            print("\n✗ Opción inválida. Intente de nuevo.\n")


if __name__ == "__main__":
    main()