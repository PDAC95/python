-- =============================================
-- CLASE 23: SQL Fundamentals
-- Base de datos: biblioteca
-- =============================================

-- Eliminar tablas si existen (para poder re-ejecutar)
DROP TABLE IF EXISTS prestamos;
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS libros;

-- =============================================
-- CREAR TABLAS
-- =============================================

CREATE TABLE libros (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    isbn TEXT UNIQUE,
    anio INTEGER,
    disponible INTEGER DEFAULT 1
);

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    fecha_registro TEXT DEFAULT CURRENT_DATE
);

CREATE TABLE prestamos (
    id INTEGER PRIMARY KEY,
    libro_id INTEGER NOT NULL,
    usuario_id INTEGER NOT NULL,
    fecha_prestamo TEXT DEFAULT CURRENT_DATE,
    fecha_devolucion TEXT
);

-- =============================================
-- INSERTAR DATOS DE EJEMPLO
-- =============================================

INSERT INTO libros (titulo, autor, isbn, anio) VALUES
    ('1984', 'George Orwell', 'ISBN001', 1949),
    ('Cien anos de soledad', 'Gabriel Garcia Marquez', 'ISBN002', 1967),
    ('El principito', 'Antoine de Saint-Exupery', 'ISBN003', 1943),
    ('Don Quijote', 'Miguel de Cervantes', 'ISBN004', 1605),
    ('Orgullo y prejuicio', 'Jane Austen', 'ISBN005', 1813);

INSERT INTO usuarios (nombre, email) VALUES
    ('Ana Garcia', 'ana@email.com'),
    ('Carlos Lopez', 'carlos@email.com'),
    ('Maria Rodriguez', 'maria@email.com');

-- =============================================
-- CONSULTAS DE EJEMPLO
-- =============================================

-- Ver todos los libros
SELECT * FROM libros;

-- Ver todos los usuarios
SELECT * FROM usuarios;

-- Libros disponibles
SELECT titulo, autor FROM libros WHERE disponible = 1;

-- Buscar por autor
SELECT * FROM libros WHERE autor LIKE '%Garcia%';

-- =============================================
-- EJERCICIOS PARA PRACTICAR
-- =============================================

-- 1. Mostrar solo titulos y autores de libros anteriores a 1950

-- 2. Buscar usuarios cuyo email contenga 'gmail'

-- 3. Contar cuantos libros hay (adelanto: SELECT COUNT(*) FROM libros)

-- 4. Marcar un libro como no disponible

-- 5. Crear un registro de prestamo
