"""
Clase 25: Solución de ejercicios de SQLite
"""
import sqlite3


def conectar():
    """Crea y retorna una conexión a biblioteca.db con row_factory."""
    conexion = sqlite3.connect('biblioteca.db')
    conexion.row_factory = sqlite3.Row
    return conexion


def contar_libros():
    """Retorna el número total de libros."""
    with conectar() as con:
        cursor = con.cursor()
        cursor.execute('SELECT COUNT(*) as total FROM libros')
        return cursor.fetchone()['total']


def buscar_por_autor(autor):
    """Busca libros de un autor específico. Retorna lista de títulos."""
    with conectar() as con:
        cursor = con.cursor()
        cursor.execute(
            'SELECT titulo FROM libros WHERE autor LIKE ?',
            (f'%{autor}%',)
        )
        return [fila['titulo'] for fila in cursor.fetchall()]


def agregar_libro(titulo, autor, isbn, anio):
    """Agrega un libro y retorna su ID."""
    with conectar() as con:
        cursor = con.cursor()
        cursor.execute(
            'INSERT INTO libros (titulo, autor, isbn, anio) VALUES (?, ?, ?, ?)',
            (titulo, autor, isbn, anio)
        )
        con.commit()
        return cursor.lastrowid


def marcar_no_disponible(id):
    """Marca un libro como no disponible. Retorna True si se modificó."""
    with conectar() as con:
        cursor = con.cursor()
        cursor.execute(
            'UPDATE libros SET disponible = 0 WHERE id = ?',
            (id,)
        )
        con.commit()
        return cursor.rowcount > 0


def eliminar_libro(id):
    """Elimina un libro. Retorna True si se eliminó."""
    with conectar() as con:
        cursor = con.cursor()
        cursor.execute('DELETE FROM libros WHERE id = ?', (id,))
        con.commit()
        return cursor.rowcount > 0


# ──── Pruebas ────
if __name__ == '__main__':
    print(f"Total de libros: {contar_libros()}")

    print("\nLibros de un autor:")
    for titulo in buscar_por_autor('Orwell'):
        print(f"  {titulo}")

    nuevo_id = agregar_libro('Test', 'Test Author', 'ISBN999', 2024)
    print(f"\nNuevo libro ID: {nuevo_id}")

    print(f"Marcar no disponible: {marcar_no_disponible(nuevo_id)}")
    print(f"Eliminar: {eliminar_libro(nuevo_id)}")
