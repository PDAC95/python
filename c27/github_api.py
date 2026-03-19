"""
Clase 27: Consumir GitHub API
Ejemplo con API real
"""
import requests


def obtener_usuario(username):
    """Obtiene información de un usuario de GitHub"""
    url = f'https://api.github.com/users/{username}'

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def obtener_repos(username):
    """Obtiene repositorios de un usuario"""
    url = f'https://api.github.com/users/{username}/repos'

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


if __name__ == '__main__':
    username = input("Username de GitHub: ").strip()

    user = obtener_usuario(username)
    if user:
        print(f"\n👤 {user['name'] or username}")
        print(f"   📝 {user['bio'] or 'Sin bio'}")
        print(f"   📍 {user['location'] or 'Sin ubicación'}")
        print(f"   📦 Repos: {user['public_repos']}")
        print(f"   👥 Seguidores: {user['followers']}")

        repos = obtener_repos(username)
        if repos:
            print(f"\n📦 Top 5 repositorios:")
            repos_sorted = sorted(
                repos,
                key=lambda r: r['stargazers_count'],
                reverse=True
            )
            for repo in repos_sorted[:5]:
                print(f"   ⭐ {repo['stargazers_count']:>5} | {repo['name']}")
