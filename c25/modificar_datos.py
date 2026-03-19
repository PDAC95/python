import sqlite3

with sqlite3.connect('biblioteca.db') as conexion:
    cursor = conexion.cursor()

    # INSERT - Agregar un libro
    cursor.execute('''
        INSERT INTO libros (titulo, autor, isbn, anio)
        VALUES ('El túnel', 'Ernesto Sabato', 'ISBN011', 1948)
    ''')

    # UPDATE - Modificar un libro
    cursor.execute('''
        UPDATE libros SET disponible = 0 WHERE id = 1
    ''')

    # IMPORTANTE: Guardar los cambios
    conexion.commit()
    print("Cambios guardados")

    # Verificar
    cursor.execute('SELECT titulo FROM libros ORDER BY id DESC LIMIT 1')
    print(f"Último libro: {cursor.fetchone()[0]}")