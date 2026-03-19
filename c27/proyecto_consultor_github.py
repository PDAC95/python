"""
Clase 27: Proyecto Final
Consultor de GitHub - Programa interactivo
"""
import requests

BASE_URL = 'https://api.github.com'


def hacer_peticion(endpoint):
    """Hace petición segura a GitHub API"""
    try:
        response = requests.get(f'{BASE_URL}{endpoint}', timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            print("❌ No encontrado")
        elif response.status_code == 403:
            print("⚠️ Límite de peticiones alcanzado. Espera un momento.")
        else:
            print(f"❌ Error HTTP: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("🔌 Error de conexión. ¿Hay internet?")
    except requests.exceptions.Timeout:
        print("⏱️ La petición tardó demasiado")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
    return None


def buscar_usuario():
    """Busca información de un usuario de GitHub"""
    username = input("  Username: ").strip()
    if not username:
        print("  Username vacío")
        return

    user = hacer_peticion(f'/users/{username}')

    if user:
        print(f"\n  👤 {user['name'] or username}")
        print(f"     📝 {user['bio'] or 'Sin bio'}")
        print(f"     📍 {user['location'] or 'Sin ubicación'}")
        print(f"     📦 Repos públicos: {user['public_repos']}")
        print(f"     👥 Seguidores: {user['followers']}")
        print(f"     👤 Siguiendo: {user['following']}")
        if user.get('blog'):
            print(f"     🌐 Blog: {user['blog']}")


def ver_repos():
    """Muestra repositorios de un usuario ordenados por estrellas"""
    username = input("  Username: ").strip()
    if not username:
        print("  Username vacío")
        return

    repos = hacer_peticion(f'/users/{username}/repos')

    if repos:
        # Ordenar por estrellas (más populares primero)
        repos_ordenados = sorted(
            repos,
            key=lambda r: r['stargazers_count'],
            reverse=True
        )

        print(f"\n  📦 Repositorios de {username} ({len(repos)} total):")
        print(f"  {'─' * 45}")

        for repo in repos_ordenados[:10]:
            stars = repo['stargazers_count']
            lang = repo['language'] or 'N/A'
            print(f"  ⭐ {stars:>6} | {repo['name']:<25} | {lang}")


def ver_repo_detalle():
    """Muestra detalles de un repositorio específico"""
    owner = input("  Owner (usuario/org): ").strip()
    repo_name = input("  Nombre del repo: ").strip()

    if not owner or not repo_name:
        print("  Datos incompletos")
        return

    repo = hacer_peticion(f'/repos/{owner}/{repo_name}')

    if repo:
        print(f"\n  📦 {repo['full_name']}")
        print(f"  {'─' * 45}")
        print(f"     📝 {repo['description'] or 'Sin descripción'}")
        print(f"     ⭐ Estrellas: {repo['stargazers_count']:,}")
        print(f"     🍴 Forks: {repo['forks_count']:,}")
        print(f"     👀 Watchers: {repo['watchers_count']:,}")
        print(f"     💻 Lenguaje: {repo['language'] or 'N/A'}")
        print(f"     📅 Creado: {repo['created_at'][:10]}")
        print(f"     🔄 Último push: {repo['pushed_at'][:10]}")
        if repo.get('license') and repo['license'].get('name'):
            print(f"     📄 Licencia: {repo['license']['name']}")


def comparar_usuarios():
    """Compara seguidores de dos usuarios"""
    user1 = input("  Usuario 1: ").strip()
    user2 = input("  Usuario 2: ").strip()

    if not user1 or not user2:
        print("  Datos incompletos")
        return

    data1 = hacer_peticion(f'/users/{user1}')
    data2 = hacer_peticion(f'/users/{user2}')

    if data1 and data2:
        print(f"\n  📊 Comparación:")
        print(f"  {'─' * 45}")
        print(f"  {'Métrica':<20} {user1:<12} {user2:<12}")
        print(f"  {'─' * 45}")
        print(f"  {'Seguidores':<20} {data1['followers']:<12,} {data2['followers']:<12,}")
        print(f"  {'Siguiendo':<20} {data1['following']:<12,} {data2['following']:<12,}")
        print(f"  {'Repos públicos':<20} {data1['public_repos']:<12} {data2['public_repos']:<12}")

        ganador = user1 if data1['followers'] > data2['followers'] else user2
        print(f"\n  🏆 Más seguidores: {ganador}")


def main():
    """Menú principal del consultor"""
    print("\n  Bienvenido al Consultor de GitHub")
    print("  Consume la API de GitHub para obtener datos reales\n")

    while True:
        print("\n" + "=" * 44)
        print("   🐙 CONSULTOR DE GITHUB")
        print("=" * 44)
        print("   1. Buscar usuario")
        print("   2. Ver repositorios de un usuario")
        print("   3. Ver detalles de un repositorio")
        print("   4. Comparar seguidores de 2 usuarios")
        print("   0. Salir")
        print("=" * 44)

        opcion = input("  Opción: ").strip()

        if opcion == '1':
            buscar_usuario()
        elif opcion == '2':
            ver_repos()
        elif opcion == '3':
            ver_repo_detalle()
        elif opcion == '4':
            comparar_usuarios()
        elif opcion == '0':
            print("\n  ¡Hasta luego! 👋")
            break
        else:
            print("  Opción no válida")


if __name__ == '__main__':
    main()
