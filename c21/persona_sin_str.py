class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"hola, soy {self.nombre} y tengo {self.edad} años"
    
    def __repr__(self):
        return f"Persona({self.nombre!r}, {self.edad!r})"

persona = Persona("Juan", 30)
print(str(persona))
print(repr(persona))

