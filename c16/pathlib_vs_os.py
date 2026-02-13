# ============================================
# Comparación: pathlib vs os.path
# ============================================

from pathlib import Path
import os

print("=== CREAR RUTAS ===")

# os.path (clásico)
ruta_os = os.path.join("datos", "reportes", "2024")
print(f"os.path: {ruta_os}")

# pathlib (moderno)
ruta_path = Path("datos") / "reportes" / "2024"
print(f"pathlib: {ruta_path}")

print("\n=== VERIFICAR EXISTENCIA ===")

archivo = "ejemplo.txt"
print(f"os.path.exists: {os.path.exists(archivo)}")
print(f"pathlib exists: {Path(archivo).exists()}")

print("\n=== OBTENER PARTES ===")

ruta = "datos/reporte_final.txt"

# os.path
print(f"os.path.basename: {os.path.basename(ruta)}")
print(f"os.path.dirname: {os.path.dirname(ruta)}")
print(f"os.path.splitext: {os.path.splitext(ruta)}")

# pathlib
p = Path(ruta)
print(f"pathlib .name: {p.name}")
print(f"pathlib .parent: {p.parent}")
print(f"pathlib .stem: {p.stem}")
print(f"pathlib .suffix: {p.suffix}")

print("\n=== RECOMENDACIÓN ===")
print("Usa pathlib para código nuevo.")
print("Entiende os.path para leer código existente.")
