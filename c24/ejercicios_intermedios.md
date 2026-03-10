# Ejercicios SQL Intermedio - Clase 24

## Instrucciones
- Usa la base de datos **biblioteca.db** en DB Browser for SQLite
- Intenta resolver cada ejercicio antes de mirar la solución
- Los ejercicios van de menor a mayor dificultad

---

## Nivel 1: ORDER BY y LIMIT

### Ejercicio 1.1
Muestra todos los libros ordenados alfabéticamente por título.

<details>
<summary>Solución</summary>

```sql
SELECT titulo, autor, anio
FROM libros
ORDER BY titulo;
```
</details>

### Ejercicio 1.2
Muestra los 3 libros más recientes (por año de publicación).

<details>
<summary>Solución</summary>

```sql
SELECT titulo, anio
FROM libros
ORDER BY anio DESC
LIMIT 3;
```
</details>

### Ejercicio 1.3
Muestra los libros de García Márquez ordenados del más viejo al más nuevo.

<details>
<summary>Solución</summary>

```sql
SELECT titulo, anio
FROM libros
WHERE autor LIKE '%García Márquez%'
ORDER BY anio;
```
</details>

### Ejercicio 1.4
Simula la "página 2" de resultados mostrando los libros del 4to al 6to (ordenados por título).

<details>
<summary>Solución</summary>

```sql
SELECT titulo
FROM libros
ORDER BY titulo
LIMIT 3 OFFSET 3;
```
</details>

### Ejercicio 1.5
Muestra los 5 libros disponibles más viejos.

<details>
<summary>Solución</summary>

```sql
SELECT titulo, anio
FROM libros
WHERE disponible = 1
ORDER BY anio
LIMIT 5;
```
</details>

---

## Nivel 2: Funciones Agregadas

### Ejercicio 2.1
¿Cuántos libros hay en total en la biblioteca?

<details>
<summary>Solución</summary>

```sql
SELECT COUNT(*) AS total_libros
FROM libros;
```
</details>

### Ejercicio 2.2
¿Cuántos libros están disponibles y cuántos están prestados? (Usa dos consultas separadas.)

<details>
<summary>Solución</summary>

```sql
-- Disponibles
SELECT COUNT(*) AS disponibles
FROM libros
WHERE disponible = 1;

-- Prestados
SELECT COUNT(*) AS prestados
FROM libros
WHERE disponible = 0;
```
</details>

### Ejercicio 2.3
¿Cuál es el libro más viejo y el más nuevo? Muestra el año mínimo y máximo.

<details>
<summary>Solución</summary>

```sql
SELECT
    MIN(anio) AS libro_mas_viejo,
    MAX(anio) AS libro_mas_nuevo
FROM libros;
```
</details>

### Ejercicio 2.4
¿Cuál es el año promedio de publicación de los libros del siglo XX (1900-1999)?

<details>
<summary>Solución</summary>

```sql
SELECT AVG(anio) AS promedio_siglo_xx
FROM libros
WHERE anio >= 1900 AND anio <= 1999;
```
</details>

### Ejercicio 2.5
¿Cuántos autores diferentes hay en la base de datos?

<details>
<summary>Solución</summary>

```sql
SELECT COUNT(DISTINCT autor) AS autores_unicos
FROM libros;
```
</details>

---

## Nivel 3: GROUP BY y HAVING

### Ejercicio 3.1
Cuenta cuántos libros tiene cada autor.

<details>
<summary>Solución</summary>

```sql
SELECT autor, COUNT(*) AS cantidad
FROM libros
GROUP BY autor;
```
</details>

### Ejercicio 3.2
Cuenta cuántos libros hay por cada estado (disponible / no disponible), ordenado por cantidad.

<details>
<summary>Solución</summary>

```sql
SELECT
    CASE disponible
        WHEN 1 THEN 'Disponible'
        ELSE 'Prestado'
    END AS estado,
    COUNT(*) AS cantidad
FROM libros
GROUP BY disponible
ORDER BY cantidad DESC;
```
</details>

### Ejercicio 3.3
Muestra los autores que tienen más de 1 libro en la base de datos.

<details>
<summary>Solución</summary>

```sql
SELECT autor, COUNT(*) AS cantidad
FROM libros
GROUP BY autor
HAVING cantidad > 1;
```
</details>

### Ejercicio 3.4
Por cada autor, muestra cuántos libros tiene, el año del más viejo y el del más nuevo. Ordena por cantidad de libros (mayor primero).

<details>
<summary>Solución</summary>

```sql
SELECT
    autor,
    COUNT(*) AS cantidad,
    MIN(anio) AS libro_mas_viejo,
    MAX(anio) AS libro_mas_nuevo
FROM libros
GROUP BY autor
ORDER BY cantidad DESC;
```
</details>

### Ejercicio 3.5
Cuenta los préstamos por mes. (Pista: usa substr para extraer el mes de la fecha.)

<details>
<summary>Solución</summary>

```sql
SELECT
    substr(fecha_prestamo, 1, 7) AS mes,
    COUNT(*) AS prestamos
FROM prestamos
GROUP BY substr(fecha_prestamo, 1, 7)
ORDER BY mes;
```
</details>

---

## Nivel 4: INNER JOIN

### Ejercicio 4.1
Muestra todos los préstamos con el título del libro (en lugar del libro_id).

<details>
<summary>Solución</summary>

```sql
SELECT l.titulo, p.fecha_prestamo
FROM prestamos p
INNER JOIN libros l ON p.libro_id = l.id;
```
</details>

### Ejercicio 4.2
Muestra todos los préstamos con el título del libro Y el nombre del usuario.

<details>
<summary>Solución</summary>

```sql
SELECT l.titulo, u.nombre, p.fecha_prestamo
FROM prestamos p
INNER JOIN libros l ON p.libro_id = l.id
INNER JOIN usuarios u ON p.usuario_id = u.id;
```
</details>

### Ejercicio 4.3
¿Qué libros tiene prestados "Ana García"?

<details>
<summary>Solución</summary>

```sql
SELECT l.titulo, p.fecha_prestamo
FROM prestamos p
INNER JOIN libros l ON p.libro_id = l.id
INNER JOIN usuarios u ON p.usuario_id = u.id
WHERE u.nombre = 'Ana García';
```
</details>

### Ejercicio 4.4
¿Cuántos libros tiene prestados cada usuario? Ordena del que más tiene al que menos.

<details>
<summary>Solución</summary>

```sql
SELECT u.nombre, COUNT(*) AS libros_prestados
FROM prestamos p
INNER JOIN usuarios u ON p.usuario_id = u.id
GROUP BY u.nombre
ORDER BY libros_prestados DESC;
```
</details>

### Ejercicio 4.5
Muestra los préstamos de febrero 2024, con título y nombre del usuario.

<details>
<summary>Solución</summary>

```sql
SELECT l.titulo, u.nombre, p.fecha_prestamo
FROM prestamos p
INNER JOIN libros l ON p.libro_id = l.id
INNER JOIN usuarios u ON p.usuario_id = u.id
WHERE p.fecha_prestamo LIKE '2024-02%'
ORDER BY p.fecha_prestamo;
```
</details>

---

## Nivel 5: Desafíos (Combinando todo)

### Ejercicio 5.1
¿Cuál es el usuario que más libros tiene prestados? Muestra solo ese usuario.

<details>
<summary>Solución</summary>

```sql
SELECT u.nombre, COUNT(*) AS total
FROM prestamos p
INNER JOIN usuarios u ON p.usuario_id = u.id
GROUP BY u.nombre
ORDER BY total DESC
LIMIT 1;
```
</details>

### Ejercicio 5.2
Muestra un reporte con el nombre de cada usuario y los títulos de los libros que tiene prestados (todos en una fila, separados por coma).

<details>
<summary>Solución</summary>

```sql
SELECT
    u.nombre,
    COUNT(*) AS total_prestamos,
    GROUP_CONCAT(l.titulo, ', ') AS libros
FROM prestamos p
INNER JOIN usuarios u ON p.usuario_id = u.id
INNER JOIN libros l ON p.libro_id = l.id
GROUP BY u.nombre;
```
</details>

### Ejercicio 5.3
Muestra los autores cuyos libros han sido prestados al menos una vez, y cuántas veces en total.

<details>
<summary>Solución</summary>

```sql
SELECT l.autor, COUNT(*) AS veces_prestado
FROM prestamos p
INNER JOIN libros l ON p.libro_id = l.id
GROUP BY l.autor
ORDER BY veces_prestado DESC;
```
</details>

### Ejercicio 5.4 (BONUS - LEFT JOIN)
Muestra los usuarios que NO tienen ningún préstamo activo.

<details>
<summary>Solución</summary>

```sql
SELECT u.nombre
FROM usuarios u
LEFT JOIN prestamos p ON u.id = p.usuario_id
WHERE p.id IS NULL;
```

Nota: LEFT JOIN incluye TODOS los usuarios, incluso si no tienen préstamos. Los que no tienen préstamos tendrán NULL en las columnas de prestamos. Con WHERE p.id IS NULL filtramos solo esos.
</details>

### Ejercicio 5.5 (BONUS - LEFT JOIN)
Muestra TODOS los libros y, si están prestados, a quién. Los no prestados deben mostrar "Disponible".

<details>
<summary>Solución</summary>

```sql
SELECT
    l.titulo,
    COALESCE(u.nombre, 'Disponible') AS estado
FROM libros l
LEFT JOIN prestamos p ON l.id = p.libro_id
LEFT JOIN usuarios u ON p.usuario_id = u.id;
```

Nota: COALESCE devuelve el primer valor no NULL. Si no hay usuario (porque no hay préstamo), devuelve 'Disponible'.
</details>

---

## Para practicar en casa

Crea una nueva tabla "categorias" y agrega una columna categoria_id a libros. Luego practica JOINs con 3 tablas.

```sql
-- Crear tabla de categorías
CREATE TABLE categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);

-- Insertar categorías
INSERT INTO categorias (nombre) VALUES
    ('Novela'),
    ('Ciencia Ficción'),
    ('Realismo Mágico'),
    ('Poesía'),
    ('Ensayo');

-- Agregar columna a libros
ALTER TABLE libros ADD COLUMN categoria_id INTEGER;

-- Asignar categorías (ajusta según tus libros)
UPDATE libros SET categoria_id = 1 WHERE id IN (4, 6, 7);
UPDATE libros SET categoria_id = 2 WHERE id IN (1, 5);
UPDATE libros SET categoria_id = 3 WHERE id IN (2, 3, 8, 9);
UPDATE libros SET categoria_id = 5 WHERE id = 10;
```

Luego intenta: "¿Cuántos libros hay por categoría?" y "¿Qué categorías tienen libros prestados?"
