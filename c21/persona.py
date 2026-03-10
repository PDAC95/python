class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, otro):
        if not isinstance(otro, Persona):
            return False
        return self.nombre == otro.nombre and self.edad == otro.edad

    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"

equipo = [
    Persona("Ana", 25),
    Persona("Carlos", 30),
    Persona("María", 22),
    Persona("Ana", 25)
]

buscar = Persona("Ana", 25)
if buscar in equipo:
    print("Ana está en el equipo")

print(f"Cuántas Anas: {equipo.count(Persona('Ana', 25))}")

equipo.remove(Persona("Ana", 25))
print(f"Después de eliminar: {equipo}")