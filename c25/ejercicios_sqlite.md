# Ejercicios - Clase 25: SQLite con Python

## Ejercicios para clase

### Ejercicio 1: Conexión básica
Conéctate a `biblioteca.db` y muestra los primeros 3 libros (título y autor).

**Pista:** Usa `LIMIT 3` en tu query.

<details>
<summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect('biblioteca.db') as conexion:
    cursor = conexion.cursor()
    cursor.execute('SELECT titulo, autor FROM libros LIMIT 3')
    for titulo, autor in cursor.fetchall():
        print(f"{titulo} - {autor}")
```
</details>

---

### Ejercicio 2: Consultas con row_factory
Usa `row_factory = sqlite3.Row` para mostrar todos los libros disponibles con formato:
```
[✓] 1984 - George Orwell (1949)
```

<details>
<summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect('biblioteca.db') as conexion:
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM libros WHERE disponible = 1')
    for libro in cursor.fetchall():
        print(f"[✓] {libro['titulo']} - {libro['autor']} ({libro['anio']})")
```
</details>

---

### Ejercicio 3: Contar registros
Muestra cuántos libros hay en total y cuántos están disponibles.

**Pista:** `SELECT COUNT(*) as total FROM libros WHERE ...`

<details>
<summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect('biblioteca.db') as conexion:
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()

    cursor.execute('SELECT COUNT(*) as total FROM libros')
    print(f"Total: {cursor.fetchone()['total']}")

    cursor.execute('SELECT COUNT(*) as total FROM libros WHERE disponible = 1')
    print(f"Disponibles: {cursor.fetchone()['total']}")
```
</details>

---

### Ejercicio 4: INSERT con parámetros seguros
Agrega un libro nuevo usando parámetros `?` y muestra el ID asignado.

<details>
<summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect('biblioteca.db') as conexion:
    cursor = conexion.cursor()
    cursor.execute(
        'INSERT INTO libros (titulo, autor, isbn, anio) VALUES (?, ?, ?, ?)',
        ('Rayuela', 'Julio Cortázar', 'ISBN020', 1963)
    )
    conexion.commit()
    print(f"Libro creado con ID: {cursor.lastrowid}")
```
</details>

---

### Ejercicio 5: UPDATE y DELETE
1. Actualiza el título de un libro existente.
2. Elimina un libro y verifica con `rowcount`.

<details>
<summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect('biblioteca.db') as conexion:
    cursor = conexion.cursor()

    # UPDATE
    cursor.execute(
        'UPDATE libros SET titulo = ? WHERE id = ?',
        ('1984 (Edición especial)', 1)
    )
    conexion.commit()
    print(f"Filas actualizadas: {cursor.rowcount}")

    # DELETE
    cursor.execute('DELETE FROM libros WHERE id = ?', (99,))
    conexion.commit()
    if cursor.rowcount > 0:
        print("Libro eliminado")
    else:
        print("No se encontró el libro")
```
</details>

---

## Ejercicios para casa

### Ejercicio 6: Función de búsqueda
Crea una función `buscar_libros(termino)` que busque en título Y autor.
Debe usar `LIKE` con parámetros seguros y retornar una lista de diccionarios.

<details>
<summary>Solución</summary>

```python
import sqlite3

def buscar_libros(termino):
    with sqlite3.connect('biblioteca.db') as conexion:
        conexion.row_factory = sqlite3.Row
        cursor = conexion.cursor()
        busqueda = f'%{termino}%'
        cursor.execute('''
            SELECT * FROM libros
            WHERE titulo LIKE ? OR autor LIKE ?
        ''', (busqueda, busqueda))
        return [dict(fila) for fila in cursor.fetchall()]

# Prueba
for libro in buscar_libros('garcía'):
    print(f"{libro['titulo']} - {libro['autor']}")
```
</details>

---

### Ejercicio 7: Parámetros nombrados
Reescribe el INSERT del ejercicio 4 usando parámetros nombrados (`:nombre`)
en lugar de `?`. Pasa los datos como diccionario.

<details>
<summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect('biblioteca.db') as conexion:
    cursor = conexion.cursor()

    libro = {
        'titulo': 'Pedro Páramo',
        'autor': 'Juan Rulfo',
        'isbn': 'ISBN021',
        'anio': 1955
    }

    cursor.execute('''
        INSERT INTO libros (titulo, autor, isbn, anio)
        VALUES (:titulo, :autor, :isbn, :anio)
    ''', libro)

    conexion.commit()
    print(f"Libro creado con ID: {cursor.lastrowid}")
```
</details>

---

### Ejercicio 8: Clase GestorUsuarios
Crea una clase `GestorUsuarios` similar a `BibliotecaDB` pero para la tabla `usuarios`.

Métodos requeridos:
- `agregar_usuario(nombre, email)` → retorna ID
- `obtener_usuario(id)` → retorna dict o None
- `listar_usuarios()` → retorna lista de dicts
- `buscar_por_nombre(nombre)` → retorna lista
- `actualizar_email(id, nuevo_email)` → retorna True/False
- `eliminar_usuario(id)` → retorna True/False

<details>
<summary>Solución</summary>

```python
import sqlite3

class GestorUsuarios:
    def __init__(self, db_path='biblioteca.db'):
        self.db_path = db_path

    def _conectar(self):
        conexion = sqlite3.connect(self.db_path)
        conexion.row_factory = sqlite3.Row
        return conexion

    def agregar_usuario(self, nombre, email):
        with self._conectar() as con:
            cursor = con.cursor()
            cursor.execute(
                'INSERT INTO usuarios (nombre, email) VALUES (?, ?)',
                (nombre, email)
            )
            con.commit()
            return cursor.lastrowid

    def obtener_usuario(self, id):
        with self._conectar() as con:
            cursor = con.cursor()
            cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id,))
            fila = cursor.fetchone()
            return dict(fila) if fila else None

    def listar_usuarios(self):
        with self._conectar() as con:
            cursor = con.cursor()
            cursor.execute('SELECT * FROM usuarios ORDER BY nombre')
            return [dict(fila) for fila in cursor.fetchall()]

    def buscar_por_nombre(self, nombre):
        with self._conectar() as con:
            cursor = con.cursor()
            cursor.execute(
                'SELECT * FROM usuarios WHERE nombre LIKE ?',
                (f'%{nombre}%',)
            )
            return [dict(fila) for fila in cursor.fetchall()]

    def actualizar_email(self, id, nuevo_email):
        with self._conectar() as con:
            cursor = con.cursor()
            cursor.execute(
                'UPDATE usuarios SET email = ? WHERE id = ?',
                (nuevo_email, id)
            )
            con.commit()
            return cursor.rowcount > 0

    def eliminar_usuario(self, id):
        with self._conectar() as con:
            cursor = con.cursor()
            cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
            con.commit()
            return cursor.rowcount > 0


# Prueba
if __name__ == '__main__':
    gestor = GestorUsuarios()

    print("=== USUARIOS ===")
    for u in gestor.listar_usuarios():
        print(f"  {u['nombre']} - {u['email']}")
```
</details>

---

### Ejercicio 9: executemany (insertar varios)
Usa `cursor.executemany()` para insertar 5 libros de una sola vez.
Pasa una lista de tuplas.

<details>
<summary>Solución</summary>

```python
import sqlite3

libros_nuevos = [
    ('La Odisea', 'Homero', 'ISBN030', -800),
    ('Don Quijote', 'Miguel de Cervantes', 'ISBN031', 1605),
    ('Hamlet', 'William Shakespeare', 'ISBN032', 1601),
    ('Crimen y castigo', 'Fiódor Dostoyevski', 'ISBN033', 1866),
    ('El principito', 'Antoine de Saint-Exupéry', 'ISBN034', 1943),
]

with sqlite3.connect('biblioteca.db') as conexion:
    cursor = conexion.cursor()
    cursor.executemany(
        'INSERT INTO libros (titulo, autor, isbn, anio) VALUES (?, ?, ?, ?)',
        libros_nuevos
    )
    conexion.commit()
    print(f"Se insertaron {cursor.rowcount} libros")
```
</details>

---

### Ejercicio 10: Manejo de errores
Agrega `try/except` a las funciones CRUD para manejar errores comunes:
- `sqlite3.IntegrityError` (ISBN duplicado)
- `sqlite3.OperationalError` (tabla no existe)

<details>
<summary>Solución</summary>

```python
import sqlite3

def agregar_libro_seguro(titulo, autor, isbn, anio):
    """Agrega un libro con manejo de errores."""
    try:
        with sqlite3.connect('biblioteca.db') as con:
            cursor = con.cursor()
            cursor.execute(
                'INSERT INTO libros (titulo, autor, isbn, anio) VALUES (?, ?, ?, ?)',
                (titulo, autor, isbn, anio)
            )
            con.commit()
            return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Error: Ya existe un libro con ISBN '{isbn}'")
        return None
    except sqlite3.OperationalError as e:
        print(f"Error de base de datos: {e}")
        return None

# Prueba - intentar insertar con ISBN duplicado
id1 = agregar_libro_seguro('Test', 'Autor', 'ISBN001', 2024)
id2 = agregar_libro_seguro('Test 2', 'Autor 2', 'ISBN001', 2024)  # Duplicado
print(f"Primer intento: ID={id1}")
print(f"Segundo intento: ID={id2}")  # None
```
</details>
