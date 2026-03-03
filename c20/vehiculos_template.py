"""
Clase 20 - Herencia: EJERCICIO 1 — Template para alumnos
=========================================================
Archivo: ejercicio1_template.py

Instrucciones:
- Completa las clases siguiendo los comentarios # TODO:
- Vehiculo es la clase PADRE
- Coche y Moto son clases HIJAS que heredan de Vehiculo
- Usa super().__init__() para llamar al constructor del padre
"""


# ============================================================
# Clase padre: Vehiculo
# ============================================================

class Vehiculo:
    def __init__(self, marca, modelo, año):
        # TODO: Guardar marca, modelo y año como atributos
        pass

    def encender(self):
        # TODO: Imprimir "El [marca] [modelo] está encendido"
        pass


# ============================================================
# Clase hija: Coche
# Hereda de Vehiculo y agrega: puertas
# ============================================================

class Coche:  # TODO: Agregar la herencia de Vehiculo
    def __init__(self, marca, modelo, año, puertas):
        # TODO: Llamar al __init__ del padre con super()
        # TODO: Guardar puertas como atributo propio
        pass

    def abrir_puerta(self):
        # TODO: Imprimir "Abriendo puerta del [marca]"
        pass


# ============================================================
# Clase hija: Moto
# Hereda de Vehiculo y agrega: cilindrada
# ============================================================

class Moto:  # TODO: Agregar la herencia de Vehiculo
    def __init__(self, marca, modelo, año, cilindrada):
        # TODO: Llamar al __init__ del padre con super()
        # TODO: Guardar cilindrada como atributo propio
        pass

    def hacer_caballito(self):
        # TODO: Imprimir "¡[marca] haciendo caballito!"
        pass


# ============================================================
# Pruebas — NO modificar esta sección
# Si tu código es correcto, esto debería funcionar sin errores
# ============================================================

if __name__ == "__main__":

    print("Probando Coche...")
    mi_coche = Coche("Toyota", "Corolla", 2022, 4)
    mi_coche.encender()       # El Toyota Corolla está encendido
    mi_coche.abrir_puerta()   # Abriendo puerta del Toyota
    print(f"Puertas: {mi_coche.puertas}")  # 4

    print()

    print("Probando Moto...")
    mi_moto = Moto("Honda", "CBR", 2021, 600)
    mi_moto.encender()          # El Honda CBR está encendido
    mi_moto.hacer_caballito()   # ¡Honda haciendo caballito!
    print(f"Cilindrada: {mi_moto.cilindrada}cc")  # 600cc

    print()

    print("Verificando herencia...")
    print(f"Coche es Vehiculo: {isinstance(mi_coche, Vehiculo)}")  # True
    print(f"Moto es Vehiculo: {isinstance(mi_moto, Vehiculo)}")    # True

    print()
    print("¡Todo correcto!" if isinstance(mi_coche, Vehiculo) else "Revisa la herencia")
