class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

mi_perro = Mascota('odie', 'perro', 2)
el_perro_de_claudio = Mascota('odin', 'perro', 3)
mi_gato = Mascota('garfield', 'gato', 5)
mi_pajaro = Mascota('piolin', 'pajaro', 1)

print(f'{mi_perro.nombre} es un {mi_perro.especie} de {mi_perro.edad} años.')

print(f'{mi_gato.nombre} es un {mi_gato.especie} de {mi_gato.edad} años.')

print(f'{mi_pajaro.nombre} es un {mi_pajaro.especie} de {mi_pajaro.edad} años.')
