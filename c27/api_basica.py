"""
Clase 27: Introducción a requests
Primeros pasos consumiendo APIs
"""
import requests

# === EJEMPLO 1: Petición básica ===
print("=== PETICIÓN BÁSICA ===")
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print(f"Status: {response.status_code}")

if response.status_code == 200:
    post = response.json()
    print(f"Título: {post['title']}")
    print(f"Body: {post['body'][:100]}...")
    print(f"User ID: {post['userId']}")

# === EJEMPLO 2: Múltiples resultados ===
print("\n=== MÚLTIPLES POSTS ===")
response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    posts = response.json()
    print(f"Total de posts: {len(posts)}\n")

    for post in posts[:5]:
        print(f"  - {post['title'][:50]}...")

# === EJEMPLO 3: Con parámetros ===
print("\n=== POSTS FILTRADOS (usuario 1) ===")
params = {'userId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

if response.status_code == 200:
    posts = response.json()
    print(f"Posts del usuario 1: {len(posts)}\n")

    for post in posts[:3]:
        print(f"  - {post['title'][:50]}...")

# === EJEMPLO 4: Explorando JSON ===
print("\n=== EXPLORANDO USUARIO ===")
response = requests.get('https://jsonplaceholder.typicode.com/users/1')
user = response.json()

print(f"Tipo: {type(user)}")
print(f"Keys: {list(user.keys())}")
print(f"Nombre: {user['name']}")
print(f"Email: {user['email']}")
print(f"Ciudad: {user['address']['city']}")
print(f"Compañía: {user['company']['name']}")
