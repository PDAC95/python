from pathlib import Path

archivo = Path("ejemplo.txt")

archivo.write_text("Hola, este es un archivo de ejemplo.")
contenido = archivo.read_text()
print (contenido)

actual = archivo.read_text()
archivo.write_text(actual + "Nuevo contenido para el archivo.")

print(archivo.read_text())

