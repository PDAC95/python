# ============================================
# EJERCICIO 2: Organizador de archivos
# ============================================
# Organiza archivos de una carpeta por extensión
#
# Categorías sugeridas:
# - imagenes: .jpg, .png, .gif
# - documentos: .pdf, .docx, .txt
# - codigo: .py, .js, .html
# - otros: todo lo demás

from pathlib import Path
import shutil

CATEGORIAS = {
    "imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "documentos": [".pdf", ".doc", ".docx", ".xlsx", ".txt"],
    "codigo": [".py", ".js", ".html", ".css"],
}


# TODO: Implementar
def obtener_categoria(extension):
    """Retorna la categoría según la extensión."""
    pass


def organizar_carpeta(ruta):
    """Organiza los archivos de una carpeta por extensión."""
    pass


if __name__ == "__main__":
    organizar_carpeta(".")
