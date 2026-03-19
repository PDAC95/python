# Ejercicios - Clase 27: APIs y Requests

## Ejercicios de clase

### Ejercicio 1: JSONPlaceholder básico
Usando `https://jsonplaceholder.typicode.com`:
1. Obtener TODOS los usuarios (`GET /users`) y mostrar nombre + email de cada uno
2. Obtener los posts del usuario 3 (`GET /posts?userId=3`) y mostrar títulos
3. Obtener los comentarios del post 1 (`GET /comments?postId=1`), contar cuántos hay y mostrar los emails

### Ejercicio 2: Proyecto Consultor de GitHub
Crear un programa interactivo con menú que permita:
1. Buscar un usuario de GitHub y mostrar su info
2. Ver repositorios de un usuario ordenados por estrellas
3. Ver detalles de un repositorio específico
4. Comparar seguidores de 2 usuarios

Requisitos: manejo de errores, timeout, funciones separadas.

---

## Ejercicios para casa

### Ejercicio 3: Pokédex
Usando la PokeAPI (`https://pokeapi.co/api/v2/`):
1. Pedir al usuario un nombre de Pokémon
2. Mostrar: nombre, ID, tipos, altura, peso
3. Mostrar las 4 primeras habilidades (abilities)
4. Si el Pokémon no existe, mostrar mensaje de error amigable

**Bonus:** Mostrar las estadísticas base (stats) del Pokémon.

### Ejercicio 4: Comparador de clima
Usando Open-Meteo (`https://api.open-meteo.com/v1/forecast`):
1. Crear un diccionario con al menos 5 ciudades y sus coordenadas
2. Consultar el clima actual de todas las ciudades
3. Mostrar una tabla comparativa con temperatura y viento
4. Indicar cuál es la ciudad más caliente y la más fría

**Bonus:** Agregar el pronóstico para mañana usando el parámetro `daily`.

### Ejercicio 5: Explorador de APIs
Elegir UNA de estas APIs y crear un programa interactivo:
- **Random User** (`https://randomuser.me/api/`): Generar perfiles aleatorios
- **Dog CEO** (`https://dog.ceo/api/`): Explorar razas de perros
- **REST Countries** (`https://restcountries.com/v3.1/`): Buscar información de países

Requisitos mínimos:
- Al menos 3 funcionalidades diferentes
- Manejo de errores con try/except
- Timeout en todas las peticiones
- Menú interactivo

### Ejercicio 6: Combinando APIs
Crear un programa que combine datos de 2 APIs diferentes.

Ejemplo: Buscar un usuario de GitHub y mostrar el clima de su ubicación.
- Paso 1: Obtener la ubicación del usuario de GitHub API
- Paso 2: Usar una API de geocoding para convertir la ciudad en coordenadas
- Paso 3: Consultar el clima de esas coordenadas con Open-Meteo

**Este ejercicio es avanzado.** Es opcional pero excelente práctica.

---

## Tips para los ejercicios

1. **Siempre usar timeout:** `requests.get(url, timeout=10)`
2. **Siempre verificar status:** `if response.status_code == 200:`
3. **Explorar con pprint:** `from pprint import pprint; pprint(data)`
4. **Usar params:** `requests.get(url, params={'key': 'value'})`
5. **Manejo de errores:** Envolver peticiones en `try/except`
