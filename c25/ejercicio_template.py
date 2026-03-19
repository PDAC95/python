"""
Clase 25: Template para ejercicios de SQLite
Completa las funciones siguiendo las instrucciones en los comentarios.
"""
import sqlite3


def conectar():
    """Crea y retorna una conexión a biblioteca.db con row_factory."""
    # TODO: Crear conexión a 'biblioteca.db'
    # TODO: Configurar row_factory = sqlite3.Row
    # TODO: Retornar la conexión
    pass


def contar_libros():
    """Retorna el número total de libros."""
    # TODO: Usar SELECT COUNT(*) FROM libros
    # TODO: Retornar el número
    pass


def buscar_por_autor(autor):
    """Busca libros de un autor específico. Retorna lista de títulos."""
    # TODO: Usar SELECT con WHERE autor LIKE ?
    # TODO: Usar parámetros seguros (?)
    # TODO: Retornar lista de títulos
    pass


def agregar_libro(titulo, autor, isbn, anio):
    """Agrega un libro y retorna su ID."""
    # TODO: Usar INSERT INTO con parámetros (?)
    # TODO: No olvidar commit()
    # TODO: Retornar cursor.lastrowid
    pass


def marcar_no_disponible(id):
    """Marca un libro como no disponible. Retorna True si se modificó."""
    # TODO: Usar UPDATE con WHERE id = ?
    # TODO: No olvidar commit()
    # TODO: Retornar cursor.rowcount > 0
    pass


def eliminar_libro(id):
    """Elimina un libro. Retorna True si se eliminó."""
    # TODO: Usar DELETE con WHERE id = ?
    # TODO: No olvidar commit()
    # TODO: Retornar cursor.rowcount > 0
    pass


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
