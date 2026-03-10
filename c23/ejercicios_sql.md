# Ejercicios SQL - Clase 23: SQL Fundamentals

## Instrucciones
- Usa la base de datos biblioteca.db que creamos en clase
- Si necesitas empezar de cero, ejecuta el archivo biblioteca.sql
- Intenta resolver cada ejercicio ANTES de ver la solucion

---

## NIVEL 1: SELECT basico

### Ejercicio 1.1
Muestra todos los datos de la tabla libros.

**Solucion:**
```sql
SELECT * FROM libros;
```

### Ejercicio 1.2
Muestra solo el titulo y el autor de cada libro.

**Solucion:**
```sql
SELECT titulo, autor FROM libros;
```

### Ejercicio 1.3
Muestra los nombres y emails de todos los usuarios.

**Solucion:**
```sql
SELECT nombre, email FROM usuarios;
```

### Ejercicio 1.4
Muestra los titulos de los libros renombrados como "nombre_libro".

**Solucion:**
```sql
SELECT titulo AS nombre_libro FROM libros;
```

---

## NIVEL 2: WHERE (filtros)

### Ejercicio 2.1
Muestra los libros publicados antes de 1900.

**Solucion:**
```sql
SELECT * FROM libros WHERE anio < 1900;
```

### Ejercicio 2.2
Busca el libro con ISBN 'ISBN003'.

**Solucion:**
```sql
SELECT * FROM libros WHERE isbn = 'ISBN003';
```

### Ejercicio 2.3
Muestra los libros cuyo titulo contenga la palabra "de".

**Solucion:**
```sql
SELECT * FROM libros WHERE titulo LIKE '%de%';
```

### Ejercicio 2.4
Muestra los libros publicados entre 1900 y 1970.

**Solucion:**
```sql
SELECT * FROM libros WHERE anio BETWEEN 1900 AND 1970;
```

### Ejercicio 2.5
Muestra los libros que sean de George Orwell O de Jane Austen.

**Solucion:**
```sql
SELECT * FROM libros
WHERE autor = 'George Orwell' OR autor = 'Jane Austen';
```

### Ejercicio 2.6
Muestra los libros publicados en los anios 1943, 1949 o 1967.

**Solucion:**
```sql
SELECT * FROM libros WHERE anio IN (1943, 1949, 1967);
```

---

## NIVEL 3: INSERT

### Ejercicio 3.1
Agrega el libro "Rayuela" de Julio Cortazar, ISBN006, publicado en 1963.

**Solucion:**
```sql
INSERT INTO libros (titulo, autor, isbn, anio)
VALUES ('Rayuela', 'Julio Cortazar', 'ISBN006', 1963);
```

### Ejercicio 3.2
Agrega un nuevo usuario: "Pedro Sanchez", email "pedro@email.com".

**Solucion:**
```sql
INSERT INTO usuarios (nombre, email)
VALUES ('Pedro Sanchez', 'pedro@email.com');
```

### Ejercicio 3.3
Agrega 2 libros mas de una sola vez (los que quieras).

**Solucion:**
```sql
INSERT INTO libros (titulo, autor, isbn, anio)
VALUES
    ('La sombra del viento', 'Carlos Ruiz Zafon', 'ISBN007', 2001),
    ('Como agua para chocolate', 'Laura Esquivel', 'ISBN008', 1989);
```

---

## NIVEL 4: UPDATE

### Ejercicio 4.1
Marca el libro con id 3 como no disponible.

**Solucion:**
```sql
UPDATE libros SET disponible = 0 WHERE id = 3;
```

### Ejercicio 4.2
Cambia el email de Ana Garcia a "ana.garcia@gmail.com".

**Solucion:**
```sql
UPDATE usuarios SET email = 'ana.garcia@gmail.com'
WHERE nombre = 'Ana Garcia';
```

### Ejercicio 4.3
Actualiza el anio de publicacion de Don Quijote a 1615 (segunda parte).

**Solucion:**
```sql
UPDATE libros SET anio = 1615
WHERE titulo = 'Don Quijote';
```

---

## NIVEL 5: DELETE

### Ejercicio 5.1
Elimina el libro con id 5.

**Solucion:**
```sql
DELETE FROM libros WHERE id = 5;
```

### Ejercicio 5.2
Elimina todos los libros publicados antes de 1700.

**Solucion:**
```sql
DELETE FROM libros WHERE anio < 1700;
```

---

## NIVEL 6: Ejercicio integrador

### Ejercicio 6.1 - Flujo completo de prestamo

Realiza las siguientes operaciones en orden:

1. Verifica que libros hay disponibles
2. El usuario con id=2 (Carlos) quiere pedir prestado el libro con id=1 (1984)
3. Crea el registro de prestamo
4. Marca el libro como no disponible
5. Verifica que el libro ya no aparece como disponible
6. Carlos devuelve el libro
7. Actualiza el prestamo con la fecha de devolucion
8. Marca el libro como disponible nuevamente
9. Verifica que todo quedo bien

**Solucion:**
```sql
-- 1. Libros disponibles
SELECT * FROM libros WHERE disponible = 1;

-- 2-3. Crear prestamo
INSERT INTO prestamos (libro_id, usuario_id)
VALUES (1, 2);

-- 4. Marcar no disponible
UPDATE libros SET disponible = 0 WHERE id = 1;

-- 5. Verificar
SELECT * FROM libros WHERE disponible = 1;

-- 6-7. Devolucion
UPDATE prestamos
SET fecha_devolucion = DATE('now')
WHERE libro_id = 1 AND usuario_id = 2 AND fecha_devolucion IS NULL;

-- 8. Marcar disponible
UPDATE libros SET disponible = 1 WHERE id = 1;

-- 9. Verificar todo
SELECT * FROM libros;
SELECT * FROM prestamos;
```

---

## NIVEL 7: Desafios extra

### Desafio 7.1
Cuenta cuantos libros hay en total (pista: usa COUNT).

**Solucion:**
```sql
SELECT COUNT(*) AS total_libros FROM libros;
```

### Desafio 7.2
Muestra los libros ordenados por anio de publicacion (pista: usa ORDER BY).

**Solucion:**
```sql
SELECT * FROM libros ORDER BY anio;
```

### Desafio 7.3
Muestra cuantos libros hay disponibles y cuantos no disponibles.

**Solucion:**
```sql
SELECT disponible, COUNT(*) AS cantidad
FROM libros
GROUP BY disponible;
```

Nota: Estos desafios usan funciones que veremos en la Clase 24, pero son un buen adelanto.

---

## Recordatorio importante

- SIEMPRE usa WHERE con UPDATE y DELETE
- Los textos van entre comillas simples: 'valor'
- Los numeros van sin comillas: 42
- Guarda tu base de datos biblioteca.db para la proxima clase
