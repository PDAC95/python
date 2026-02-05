tareas = ["Estudiar Python", "Hacer ejercicio", "Comprar leche"]

with open("tareas.txt", "w") as archivo:
    for tarea in tareas:
        archivo.write(tarea + "\n")