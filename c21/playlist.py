class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar(self, cancion):
        self.canciones.append(cancion)

    def __contains__(self,cancion):
        cancion_lower = cancion.lower()
        for c in self.canciones:
            if c.lower() == cancion_lower:
                return True

mi_playlist = Playlist("Rock Clásico")
mi_playlist.agregar("Bohemian Rhapsody")
mi_playlist.agregar("Stairway to Heaven")
mi_playlist.agregar("Bed of Roses")

print("bohemian rhapsody" in mi_playlist)
print("HOTEL CALIFORNIA" in mi_playlist)
print("bed of roses" in mi_playlist)



