import sqlite3

with sqlite3.connect('biblioteca.db') as conexion:
    cursor = conexion.cursor()

    # Insertar y obtener el ID
    cursor.execute('''
        INSERT INTO libros (titulo, autor, isbn, anio)
        VALUES ('Ensayo sobre la ceguera', 'José Saramago', 'ISBN013', 1995)
    ''')

    nuevo_id = cursor.lastrowid
    print(f"✅ Libro creado con ID: {nuevo_id}")

    conexion.commit()

    # Verificar
    cursor.execute('SELECT * FROM libros WHERE id = ?', (nuevo_id,))
    libro = cursor.fetchone()
    print(f"   Título: {libro[1]}")