"""
Ejecutar este archivo ANTES de la clase para crear biblioteca.db
con datos de ejemplo en las tablas 'libros' y 'usuarios'.
"""
import sqlite3

conexion = sqlite3.connect('biblioteca.db')
cursor = conexion.cursor()

# Crear tabla libros
cursor.execute('''
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        isbn TEXT UNIQUE,
        anio INTEGER,
        disponible INTEGER DEFAULT 1
    )
''')

# Crear tabla usuarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE,
        fecha_registro TEXT DEFAULT CURRENT_DATE
    )
''')

# Insertar libros
libros = [
    ('1984', 'George Orwell', 'ISBN001', 1949, 1),
    ('Cien años de soledad', 'Gabriel García Márquez', 'ISBN002', 1967, 1),
    ('El principito', 'Antoine de Saint-Exupéry', 'ISBN003', 1943, 0),
    ('Don Quijote de la Mancha', 'Miguel de Cervantes', 'ISBN004', 1605, 1),
    ('Crónica de una muerte anunciada', 'Gabriel García Márquez', 'ISBN005', 1981, 1),
    ('La casa de los espíritus', 'Isabel Allende', 'ISBN006', 1982, 0),
    ('El amor en los tiempos del cólera', 'Gabriel García Márquez', 'ISBN007', 1985, 1),
    ('Ficciones', 'Jorge Luis Borges', 'ISBN008', 1944, 1),
    ('Rayuela', 'Julio Cortázar', 'ISBN009', 1963, 0),
    ('Pedro Páramo', 'Juan Rulfo', 'ISBN010', 1955, 1),
]

cursor.executemany('''
    INSERT OR IGNORE INTO libros (titulo, autor, isbn, anio, disponible)
    VALUES (?, ?, ?, ?, ?)
''', libros)

# Insertar usuarios
usuarios = [
    ('Ana López', 'ana.lopez@email.com'),
    ('Carlos Ruiz', 'carlos.ruiz@email.com'),
    ('María Torres', 'maria.torres@email.com'),
    ('Diego Fernández', 'diego.fernandez@email.com'),
    ('Lucía Martínez', 'lucia.martinez@email.com'),
]

cursor.executemany('''
    INSERT OR IGNORE INTO usuarios (nombre, email)
    VALUES (?, ?)
''', usuarios)

conexion.commit()
conexion.close()

print("✅ biblioteca.db creada con éxito")
print("   - 10 libros")
print("   - 5 usuarios")
