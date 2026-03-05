class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola! mi nombre es:{self.nombre}")
        print(f"tengp {self.edad} años.")
        print("¡Encantado de conocerte!")
    
    def cumplir_anios(self):
        self.edad += 1
        return f"¡Feliz cumpleaños! Ahora tienes {self.edad} años."
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.materias = []

    def presentarse(self):
        super().saludar()
        print(f"continuacion saludo.")

    def saludar(self):
        print(f"Hola! mi nombre es:{self.nombre} y estudio {self.carrera}.")

    def estudiar(self, materia):
        print(f"Inscrito en {materia}.")

    def inscribir_materia(self, materia):
        self.materias.append(materia)
        print(f"inscrito en {materia}.")

class Profesor(Persona):
    def __init__(self, nombre, edad, departamento):
        super().__init__(nombre, edad)
        self.departamento = departamento
        self.cursos = []

    def saludar(self):
        print(f"Hola! mi nombre es:{self.nombre} y trabajo en el departamento de {self.departamento}.")

    def enseñar(self, curso):
        print(f"[{self.nombre} esta ensenando {curso}.")

    def asignar_curso(self, curso):
        self.cursos.append(curso)
        print(f"Asignado a {curso}.")

# Ejemplo de uso
ana = Estudiante("Ana", 20, "Ingeniería Informática")
carlos = Profesor("Carlos", 45, "Matemáticas")

#metodos de la clase Persona
ana.saludar()
carlos.saludar()

#metodos propios
ana.estudiar("Programación")
carlos.enseñar("Álgebra")
ana.presentarse()

ana.cumplir_anios()


