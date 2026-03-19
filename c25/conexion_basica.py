import sqlite3

with sqlite3.connect('biblioteca.db') as conexion:
    # Configurar para obtener resultados tipo diccionario
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()

    cursor.execute('SELECT id, titulo, autor, anio FROM libros')

    for fila in cursor.fetchall():
        # Ahora podemos acceder por nombre
        print(f"{fila['id']}. {fila['titulo']}")
        print(f"   Autor: {fila['autor']}")
        print(f"   Año: {fila['anio']}")
        print()