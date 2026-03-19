"""
Clase 25: Diferentes formas de hacer consultas
Demuestra fetchall, fetchone, row_factory y consultas con WHERE.
"""
import sqlite3

with sqlite3.connect('biblioteca.db') as conexion:
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()

    # fetchall - todos los resultados
    print("=== Todos los libros ===")
    cursor.execute('SELECT titulo FROM libros')
    for libro in cursor.fetchall():
        print(f"  {libro['titulo']}")

    # fetchone - un solo resultado
    print("\n=== Un libro ===")
    cursor.execute('SELECT * FROM libros WHERE id = 1')
    libro = cursor.fetchone()
    if libro:
        print(f"  {libro['titulo']} de {libro['autor']}")

    # Con WHERE
    print("\n=== Libros disponibles ===")
    cursor.execute('SELECT titulo FROM libros WHERE disponible = 1')
    for libro in cursor.fetchall():
        print(f"  ✓ {libro['titulo']}")
