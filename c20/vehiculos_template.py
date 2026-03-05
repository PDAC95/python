"""
Clase 20 - Herencia: Solución Ejercicio 1 — Vehículos
======================================================
Archivo: vehiculos.py

Contenido:
- Clase padre Vehiculo con marca, modelo, año y encender()
- Clase hija Coche con puertas y abrir_puerta()
- Clase hija Moto con cilindrada y hacer_caballito()

Corresponde al slide 11 de la presentación.
"""


# ============================================================
# Clase padre
# ============================================================

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def encender(self):
        print(f"El {self.marca} {self.modelo} está encendido")


# ============================================================
# Clases hijas
# ============================================================

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas

    def abrir_puerta(self):
        print(f"Abriendo puerta del {self.marca}")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def hacer_caballito(self):
        print(f"¡{self.marca} haciendo caballito!")


# ============================================================
# Pruebas
# ============================================================

if __name__ == "__main__":

    print("=" * 50)
    print("Ejercicio 1 — Jerarquía de Vehículos")
    print("=" * 50)

    mi_coche = Coche("Toyota", "Corolla", 2022, 4)
    mi_moto = Moto("Honda", "CBR", 2021, 600)

    # Métodos heredados
    mi_coche.encender()       # El Toyota Corolla está encendido
    mi_moto.encender()        # El Honda CBR está encendido

    print()

    # Métodos propios
    mi_coche.abrir_puerta()   # Abriendo puerta del Toyota
    mi_moto.hacer_caballito() # ¡Honda haciendo caballito!

    print()

    # Verificar atributos
    print(f"Coche: {mi_coche.marca} {mi_coche.modelo} ({mi_coche.año}) - {mi_coche.puertas} puertas")
    print(f"Moto: {mi_moto.marca} {mi_moto.modelo} ({mi_moto.año}) - {mi_moto.cilindrada}cc")

    print()

    # isinstance
    print(f"mi_coche es Vehiculo: {isinstance(mi_coche, Vehiculo)}")  # True
    print(f"mi_moto es Vehiculo: {isinstance(mi_moto, Vehiculo)}")    # True
    print(f"mi_coche es Moto: {isinstance(mi_coche, Moto)}")          # False
