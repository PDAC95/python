import sqlite3

with sqlite3.connect('biblioteca.db') as conexion:
    cursor = conexion.cursor()

    # FORMA SEGURA con parámetros

    # Un parámetro
    id_buscar = 1
    cursor.execute('SELECT * FROM libros WHERE id = ?', (id_buscar,))
    print(cursor.fetchone())

    # Múltiples parámetros
    titulo = 'Nuevo libro'
    autor = 'Autor desconocido'
    cursor.execute(
        'INSERT INTO libros (titulo, autor, isbn, anio) VALUES (?, ?, ?, ?)',
        (titulo, autor, 'ISBN999', 2024)
    )

    # Con LIKE también funciona
    busqueda = '%garcía%'
    cursor.execute('SELECT titulo FROM libros WHERE autor LIKE ?', (busqueda,))
    for libro in cursor.fetchall():
        print(libro[0])

    conexion.rollback()  # Deshacer el INSERT de prueba