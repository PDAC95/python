class Cancion:
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = duracion_segundos

    def __str__(self):
        """Formato: 'Titulo - Artista (m:ss)'"""
        minutos = self.duracion_segundos // 60
        segundos = self.duracion_segundos % 60
        return f"{self.titulo} - {self.artista} ({minutos}:{segundos:02d})"

    def __repr__(self):
        """Formato técnico para recrear el objeto"""
        return f"Cancion('{self.titulo}', '{self.artista}', {self.duracion_segundos})"

    def __eq__(self, otro):
        """Dos canciones son iguales si mismo título Y artista"""
        if not isinstance(otro, Cancion):
            return False
        return self.titulo == otro.titulo and self.artista == otro.artista

    def __lt__(self, otro):
        """Ordenar por duración (menor a mayor)"""
        return self.duracion_segundos < otro.duracion_segundos


# ═══════════════════════════════════════════════════════════════
# Pruebas
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Crear canciones
    bohemian = Cancion("Bohemian Rhapsody", "Queen", 355)
    stairway = Cancion("Stairway to Heaven", "Led Zeppelin", 482)
    imagine = Cancion("Imagine", "John Lennon", 183)

    # __str__
    print("=== __str__ ===")
    print(bohemian)   # Bohemian Rhapsody - Queen (5:55)
    print(stairway)   # Stairway to Heaven - Led Zeppelin (8:02)
    print(imagine)     # Imagine - John Lennon (3:03)

    # __repr__
    print("\n=== __repr__ ===")
    print(repr(bohemian))  # Cancion('Bohemian Rhapsody', 'Queen', 355)

    # __eq__
    print("\n=== __eq__ ===")
    bohemian2 = Cancion("Bohemian Rhapsody", "Queen", 360)  # Diferente duración
    print(f"bohemian == bohemian2: {bohemian == bohemian2}")  # True (mismo título y artista)
    print(f"bohemian == imagine: {bohemian == imagine}")      # False

    # __lt__ y sort
    print("\n=== Ordenar por duración ===")
    playlist = [bohemian, stairway, imagine]
    playlist.sort()
    print("Ordenadas por duración:")
    for c in playlist:
        print(f"  {c}")

    print(f"\nMás corta: {min(playlist)}")
    print(f"Más larga: {max(playlist)}")
