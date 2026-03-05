# ═══════════════════════════════════════════════════════════════
# Clase 21 - Ejercicio 1: Clase Cancion (TEMPLATE)
# ═══════════════════════════════════════════════════════════════
# Crear una clase Cancion con los siguientes dunder methods:
#
# Atributos:
#   - titulo (string)
#   - artista (string)
#   - duracion_segundos (int)
#
# Métodos dunder:
#   - __str__  → "Titulo - Artista (m:ss)"
#   - __repr__ → "Cancion('Titulo', 'Artista', 225)"
#   - __eq__   → Dos canciones iguales si mismo título Y artista
#   - __lt__   → Ordenar por duración (menor a mayor)
#
# Pistas:
#   - minutos = segundos // 60
#   - resto   = segundos % 60
#   - f'{segundos:02d}' → formatea con cero: 5 → "05"
# ═══════════════════════════════════════════════════════════════


class Cancion:
    def __init__(self, titulo, artista, duracion_segundos):
        # TODO: guardar los atributos
        pass

    def __str__(self):
        # TODO: retornar "Titulo - Artista (m:ss)"
        pass

    def __repr__(self):
        # TODO: retornar "Cancion('Titulo', 'Artista', 225)"
        pass

    def __eq__(self, otro):
        # TODO: comparar por titulo Y artista
        # No olviden verificar isinstance()
        pass

    def __lt__(self, otro):
        # TODO: comparar por duración
        pass


# ═══════════════════════════════════════════════════════════════
# Pruebas - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    bohemian = Cancion("Bohemian Rhapsody", "Queen", 355)
    stairway = Cancion("Stairway to Heaven", "Led Zeppelin", 482)
    imagine = Cancion("Imagine", "John Lennon", 183)

    # Test __str__
    print("=== Test __str__ ===")
    print(bohemian)   # Esperado: Bohemian Rhapsody - Queen (5:55)
    print(imagine)     # Esperado: Imagine - John Lennon (3:03)

    # Test __repr__
    print("\n=== Test __repr__ ===")
    print(repr(bohemian))  # Esperado: Cancion('Bohemian Rhapsody', 'Queen', 355)

    # Test __eq__
    print("\n=== Test __eq__ ===")
    bohemian2 = Cancion("Bohemian Rhapsody", "Queen", 360)
    print(f"bohemian == bohemian2: {bohemian == bohemian2}")  # Esperado: True
    print(f"bohemian == imagine: {bohemian == imagine}")      # Esperado: False

    # Test __lt__ y sort
    print("\n=== Test ordenar ===")
    playlist = [bohemian, stairway, imagine]
    playlist.sort()
    print("Ordenadas por duración:")
    for c in playlist:
        print(f"  {c}")
    # Esperado:
    #   Imagine - John Lennon (3:03)
    #   Bohemian Rhapsody - Queen (5:55)
    #   Stairway to Heaven - Led Zeppelin (8:02)
