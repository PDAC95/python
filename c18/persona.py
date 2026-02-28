class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} tengo {self.edad} años.")

    def cumplir_años(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años.")

    def cantar(self):
        print(f"{self.nombre} está cantando una canción.")


ana = Persona("Ana", 30)
carlos = Persona("Carlos", 25)
maria = Persona("Maria", 35)


ana.edad = 99

print(ana.edad)
print(carlos.edad)

ana.saludar()
carlos.saludar()
maria.saludar()

ana.cantar()
carlos.cantar()         

      




