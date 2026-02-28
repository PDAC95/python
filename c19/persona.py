class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # Atributo privado

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def edad(self):
        if not isinstance(valor, int):
            raise ValueError("La edad debe ser un número entero.")
        if valor < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = valor

        persona = Persona("Ana", 25)
        print(f"{persona.nombre} tiene {persona.edad} años.")

        persona.edad = 30
        print(f"{persona.nombre} ahora tiene {persona.edad} años.")

        persona.edad = -5  # Intento de establecer una edad negativa

        