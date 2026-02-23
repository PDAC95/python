from pathlib import Path


def explorar_carpeta(ruta_str="."):
    """Explora una carpeta y muestra estadísticas."""
    carpeta = Path(ruta_str)

    if not carpeta.exists():
        print(f"x La carpeta '{ruta_str}' no existe")
        return

    if not carpeta.is_dir():
        print(f"x '{ruta_str}' no es una carpeta")
        return

    print(f" Contenido de: {carpeta.absolute()}")
    print("─" * 40)

    extensiones = {}
    carpetas = 0
    tamano_total = 0

    for item in sorted(carpeta.iterdir()):
        if item.is_file():
            tamano = item.stat().st_size
            tamano_kb = tamano / 1024
            print(f" {item.name} ({tamano_kb:.1f} KB)")

            ext = item.suffix if item.suffix else "(sin ext)"
            extensiones[ext] = extensiones.get(ext, 0) + 1
            tamano_total += tamano
        else:
            print(f"📁 {item.name}/")
            carpetas += 1

    print(f"\n Resumen:")
    for ext, cantidad in sorted(extensiones.items()):
        print(f"  {ext}: {cantidad} archivo(s)")
    print(f"  Carpetas: {carpetas}")
    print(f"  Tamaño total: {tamano_total/1024:.1f} KB")


explorar_carpeta(".")
