import sqlite3

with sqlite3.connect('biblioteca.db') as conexion:
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()

    # 1. Todos los usuarios
    print("=== USUARIOS ===")
    cursor.execute('SELECT nombre, email FROM usuarios')
    for u in cursor.fetchall():
        print(f"{u['nombre']} - {u['email']}")

    # 2. Contar libros
    print("\n=== TOTAL LIBROS ===")
    cursor.execute('SELECT COUNT(*) as total FROM libros')
    resultado = cursor.fetchone()
    print(f"Total: {resultado['total']} libros")

    # 3. Libros del siglo XX
    print("\n=== LIBROS SIGLO XX ===")
    cursor.execute('SELECT titulo, anio FROM libros WHERE anio >= 1900 AND anio < 2000')
    for libro in cursor.fetchall():
        print(f"{libro['titulo']} ({libro['anio']})")

    # 4. Libros con "el" en título
    print("\n=== LIBROS CON 'EL' ===")
    cursor.execute("SELECT titulo FROM libros WHERE titulo LIKE '%el%'")
    for libro in cursor.fetchall():
        print(f"  {libro['titulo']}")