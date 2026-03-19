"""
Clase 25: Proyecto - Clase BibliotecaDB
Una clase que encapsula todas las operaciones de base de datos.
El código que usa esta clase no necesita saber SQL.
"""
import sqlite3


class BibliotecaDB:
    """Gestiona la base de datos de la biblioteca."""

    def __init__(self, db_path='biblioteca.db'):
        self.db_path = db_path

    def _conectar(self):
        """Crea una conexión configurada con row_factory."""
        conexion = sqlite3.connect(self.db_path)
        conexion.row_factory = sqlite3.Row
        return conexion

    # ──── CREATE ────
    def agregar_libro(self, titulo, autor, isbn, anio):
        """Agrega un libro y retorna su ID."""
        with self._conectar() as con:
            cursor = con.cursor()
            cursor.execute('''
                INSERT INTO libros (titulo, autor, isbn, anio)
                VALUES (?, ?, ?, ?)
            ''', (titulo, autor, isbn, anio))
            con.commit()
            return cursor.lastrowid

    # ──── READ ────
    def obtener_libro(self, id):
        """Obtiene un libro por ID. Retorna dict o None."""
        with self._conectar() as con:
            cursor = con.cursor()
            cursor.execute('SELECT * FROM libros WHERE id = ?', (id,))
            fila = cursor.fetchone()
            if fila:
                return dict(fila)
            return None

    def listar_libros(self):
        """Retorna lista de todos los libros como diccionarios."""
        with self._conectar() as con:
            cursor = con.cursor()
            cursor.execute('SELECT * FROM libros ORDER BY titulo')
            return [dict(fila) for fila in cursor.fetchall()]

    def buscar_libros(self, termino):
        """Busca libros por título o autor. Retorna lista."""
        with self._conectar() as con:
            cursor = con.cursor()
            busqueda = f'%{termino}%'
            cursor.execute('''
                SELECT * FROM libros
                WHERE titulo LIKE ? OR autor LIKE ?
            ''', (busqueda, busqueda))
            return [dict(fila) for fila in cursor.fetchall()]

    # ──── UPDATE ────
    def actualizar_disponibilidad(self, id, disponible):
        """Cambia la disponibilidad de un libro. Retorna True/False."""
        with self._conectar() as con:
            cursor = con.cursor()
            cursor.execute(
                'UPDATE libros SET disponible = ? WHERE id = ?',
                (1 if disponible else 0, id)
            )
            con.commit()
            return cursor.rowcount > 0

    # ──── DELETE ────
    def eliminar_libro(self, id):
        """Elimina un libro por ID. Retorna True/False."""
        with self._conectar() as con:
            cursor = con.cursor()
            cursor.execute('DELETE FROM libros WHERE id = ?', (id,))
            con.commit()
            return cursor.rowcount > 0


# ──── Ejemplo de uso ────
if __name__ == '__main__':
    bib = BibliotecaDB()

    # Listar todos
    print("=== LIBROS EN BIBLIOTECA ===")
    for libro in bib.listar_libros():
        estado = "✓" if libro['disponible'] else "✗"
        print(f"  [{estado}] {libro['titulo']} - {libro['autor']} ({libro['anio']})")

    # Buscar
    print("\n=== BUSCAR 'garcía' ===")
    resultados = bib.buscar_libros('garcía')
    if resultados:
        for libro in resultados:
            print(f"  {libro['titulo']} - {libro['autor']}")
    else:
        print("  No se encontraron resultados")

    # Agregar
    print("\n=== AGREGAR LIBRO ===")
    nuevo_id = bib.agregar_libro(
        'Rayuela', 'Julio Cortázar', 'ISBN020', 1963
    )
    print(f"  Libro agregado con ID: {nuevo_id}")

    # Obtener
    libro = bib.obtener_libro(nuevo_id)
    if libro:
        print(f"  Verificación: {libro['titulo']} de {libro['autor']}")

    # Actualizar disponibilidad
    print("\n=== ACTUALIZAR DISPONIBILIDAD ===")
    if bib.actualizar_disponibilidad(nuevo_id, False):
        print(f"  Libro {nuevo_id} marcado como no disponible")

    # Eliminar
    print("\n=== ELIMINAR LIBRO ===")
    if bib.eliminar_libro(nuevo_id):
        print(f"  Libro {nuevo_id} eliminado")
