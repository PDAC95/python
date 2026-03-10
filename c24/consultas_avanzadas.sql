-- =============================================
-- CLASE 24: SQL Intermedio
-- Consultas avanzadas para biblioteca.db
-- =============================================
-- Ejecutar en DB Browser for SQLite
-- Asegúrate de tener biblioteca.db de la Clase 23


-- =============================================
-- PREPARACIÓN: Agregar más datos
-- (Ejecutar ANTES de la clase si no se ha hecho)
-- =============================================

-- Más libros
INSERT INTO libros (titulo, autor, isbn, anio) VALUES
    ('Rayuela', 'Julio Cortázar', 'ISBN006', 1963),
    ('La sombra del viento', 'Carlos Ruiz Zafón', 'ISBN007', 2001),
    ('Crónica de una muerte anunciada', 'Gabriel García Márquez', 'ISBN008', 1981),
    ('El amor en los tiempos del cólera', 'Gabriel García Márquez', 'ISBN009', 1985),
    ('Ficciones', 'Jorge Luis Borges', 'ISBN010', 1944);

-- Más usuarios
INSERT INTO usuarios (nombre, email) VALUES
    ('Pedro Sánchez', 'pedro@email.com'),
    ('Laura Martínez', 'laura@email.com');

-- Algunos préstamos
INSERT INTO prestamos (libro_id, usuario_id, fecha_prestamo) VALUES
    (1, 1, '2024-01-15'),
    (2, 1, '2024-01-20'),
    (3, 2, '2024-02-01'),
    (6, 3, '2024-02-10'),
    (7, 4, '2024-02-15');

-- Marcar libros prestados como no disponibles
UPDATE libros SET disponible = 0 WHERE id IN (1, 2, 3, 6, 7);


-- =============================================
-- SECCIÓN 1: ORDER BY Y LIMIT
-- =============================================

-- Libros ordenados por año (más viejo primero)
SELECT titulo, autor, anio
FROM libros
ORDER BY anio;

-- Libros ordenados por año (más nuevo primero)
SELECT titulo, autor, anio
FROM libros
ORDER BY anio DESC;

-- Ordenar por título (alfabéticamente)
SELECT titulo, autor
FROM libros
ORDER BY titulo;

-- Ordenar por múltiples columnas: por autor, luego por año
SELECT autor, titulo, anio
FROM libros
ORDER BY autor, anio;

-- Top 3 libros más viejos
SELECT titulo, anio
FROM libros
ORDER BY anio
LIMIT 3;

-- Top 3 libros más nuevos
SELECT titulo, anio
FROM libros
ORDER BY anio DESC
LIMIT 3;

-- Paginación: página 1 (primeros 3)
SELECT titulo FROM libros ORDER BY titulo LIMIT 3;

-- Paginación: página 2 (siguientes 3, saltando 3)
SELECT titulo FROM libros ORDER BY titulo LIMIT 3 OFFSET 3;

-- Paginación: página 3 (siguientes 3, saltando 6)
SELECT titulo FROM libros ORDER BY titulo LIMIT 3 OFFSET 6;

-- Combinando WHERE + ORDER BY + LIMIT
-- Los 2 libros más nuevos de García Márquez
SELECT titulo, anio
FROM libros
WHERE autor LIKE '%García Márquez%'
ORDER BY anio DESC
LIMIT 2;

-- Libros disponibles, ordenados por título, solo 5
SELECT titulo, autor
FROM libros
WHERE disponible = 1
ORDER BY titulo
LIMIT 5;


-- =============================================
-- SECCIÓN 2: FUNCIONES AGREGADAS
-- =============================================

-- Contar todos los libros
SELECT COUNT(*) AS total_libros FROM libros;

-- Contar libros disponibles
SELECT COUNT(*) AS disponibles
FROM libros
WHERE disponible = 1;

-- Estadísticas completas de años
SELECT
    COUNT(*) AS total_libros,
    MIN(anio) AS mas_viejo,
    MAX(anio) AS mas_nuevo,
    AVG(anio) AS promedio_anio
FROM libros;

-- Autores únicos (sin repetir)
SELECT COUNT(DISTINCT autor) AS autores_unicos FROM libros;

-- Comparar total vs únicos
SELECT
    COUNT(*) AS total_libros,
    COUNT(DISTINCT autor) AS autores_diferentes
FROM libros;

-- MIN y MAX con texto
SELECT
    MIN(titulo) AS primero_alfabeticamente,
    MAX(titulo) AS ultimo_alfabeticamente
FROM libros;

-- Funciones agregadas con WHERE
-- Libros del siglo XX en adelante
SELECT
    COUNT(*) AS cantidad,
    AVG(anio) AS promedio
FROM libros
WHERE anio >= 1900;

-- Estadísticas de García Márquez
SELECT
    COUNT(*) AS libros_garcia_marquez,
    MIN(anio) AS libro_mas_viejo,
    MAX(anio) AS libro_mas_reciente
FROM libros
WHERE autor LIKE '%García Márquez%';


-- =============================================
-- SECCIÓN 3: GROUP BY Y HAVING
-- =============================================

-- Contar libros por autor
SELECT autor, COUNT(*) AS cantidad
FROM libros
GROUP BY autor;

-- Libros por autor, ordenados por cantidad (mayor primero)
SELECT autor, COUNT(*) AS cantidad
FROM libros
GROUP BY autor
ORDER BY cantidad DESC;

-- Libros disponibles vs no disponibles
SELECT
    disponible,
    COUNT(*) AS cantidad
FROM libros
GROUP BY disponible;

-- Versión más legible con CASE
SELECT
    CASE disponible
        WHEN 1 THEN 'Disponible'
        ELSE 'Prestado'
    END AS estado,
    COUNT(*) AS cantidad
FROM libros
GROUP BY disponible;

-- Estadísticas por autor: cantidad, rango de años
SELECT
    autor,
    COUNT(*) AS cantidad,
    MIN(anio) AS desde,
    MAX(anio) AS hasta
FROM libros
GROUP BY autor
ORDER BY cantidad DESC;

-- HAVING: autores con más de 1 libro
SELECT autor, COUNT(*) AS cantidad
FROM libros
GROUP BY autor
HAVING cantidad > 1;

-- WHERE + GROUP BY + HAVING + ORDER BY juntos
SELECT autor, COUNT(*) AS cantidad
FROM libros
WHERE anio >= 1900
GROUP BY autor
HAVING cantidad >= 1
ORDER BY cantidad DESC;


-- =============================================
-- SECCIÓN 4: INNER JOIN
-- =============================================

-- Ver préstamos (solo IDs, no muy útil)
SELECT * FROM prestamos;

-- JOIN: Préstamos con título del libro
SELECT
    prestamos.id,
    libros.titulo,
    prestamos.fecha_prestamo
FROM prestamos
INNER JOIN libros ON prestamos.libro_id = libros.id;

-- JOIN doble: Préstamos con título Y nombre de usuario
SELECT
    libros.titulo,
    usuarios.nombre,
    prestamos.fecha_prestamo
FROM prestamos
INNER JOIN libros ON prestamos.libro_id = libros.id
INNER JOIN usuarios ON prestamos.usuario_id = usuarios.id;

-- JOIN con alias (más corto)
SELECT p.id, l.titulo, u.nombre, p.fecha_prestamo
FROM prestamos p
INNER JOIN libros l ON p.libro_id = l.id
INNER JOIN usuarios u ON p.usuario_id = u.id;

-- JOIN + WHERE: Préstamos de un usuario específico
SELECT l.titulo, p.fecha_prestamo
FROM prestamos p
INNER JOIN libros l ON p.libro_id = l.id
INNER JOIN usuarios u ON p.usuario_id = u.id
WHERE u.nombre = 'Ana García';

-- JOIN + ORDER BY: Préstamos ordenados por fecha
SELECT l.titulo, u.nombre, p.fecha_prestamo
FROM prestamos p
INNER JOIN libros l ON p.libro_id = l.id
INNER JOIN usuarios u ON p.usuario_id = u.id
ORDER BY p.fecha_prestamo DESC;

-- JOIN + GROUP BY: Libros prestados por usuario
SELECT u.nombre, COUNT(*) AS libros_prestados
FROM prestamos p
INNER JOIN usuarios u ON p.usuario_id = u.id
GROUP BY u.nombre
ORDER BY libros_prestados DESC;

-- JOIN + GROUP BY: Veces que se prestó cada libro
SELECT l.titulo, COUNT(*) AS veces_prestado
FROM prestamos p
INNER JOIN libros l ON p.libro_id = l.id
GROUP BY l.titulo
ORDER BY veces_prestado DESC;

-- Reporte completo con GROUP_CONCAT
SELECT
    u.nombre,
    COUNT(*) AS total_prestamos,
    GROUP_CONCAT(l.titulo, ', ') AS libros
FROM prestamos p
INNER JOIN usuarios u ON p.usuario_id = u.id
INNER JOIN libros l ON p.libro_id = l.id
GROUP BY u.nombre;


-- =============================================
-- EJERCICIOS PARA PRACTICAR
-- (Intenta resolverlos antes de ver las soluciones)
-- =============================================

-- EJERCICIO 1: Libros del siglo XX ordenados por autor
-- Tu respuesta aquí:


-- EJERCICIO 2: Los 3 autores con más libros
-- Tu respuesta aquí:


-- EJERCICIO 3: Préstamos del mes de enero 2024
-- Tu respuesta aquí:


-- EJERCICIO 4: Usuario con más préstamos
-- Tu respuesta aquí:


-- EJERCICIO 5: Libros que nunca se han prestado (LEFT JOIN)
-- Tu respuesta aquí:


-- =============================================
-- SOLUCIONES (no mirar antes de intentar)
-- =============================================

-- Solución 1:
-- SELECT titulo, autor, anio
-- FROM libros
-- WHERE anio >= 1900 AND anio <= 1999
-- ORDER BY autor;

-- Solución 2:
-- SELECT autor, COUNT(*) AS cantidad
-- FROM libros
-- GROUP BY autor
-- ORDER BY cantidad DESC
-- LIMIT 3;

-- Solución 3:
-- SELECT l.titulo, u.nombre, p.fecha_prestamo
-- FROM prestamos p
-- INNER JOIN libros l ON p.libro_id = l.id
-- INNER JOIN usuarios u ON p.usuario_id = u.id
-- WHERE p.fecha_prestamo LIKE '2024-01%';

-- Solución 4:
-- SELECT u.nombre, COUNT(*) AS total
-- FROM prestamos p
-- INNER JOIN usuarios u ON p.usuario_id = u.id
-- GROUP BY u.nombre
-- ORDER BY total DESC
-- LIMIT 1;

-- Solución 5 (BONUS - LEFT JOIN):
-- SELECT u.nombre
-- FROM usuarios u
-- LEFT JOIN prestamos p ON u.id = p.usuario_id
-- WHERE p.id IS NULL;
