"""
Clase 20 - Herencia: Ejemplos básicos
=====================================
Archivo: persona_estudiante.py

Contenido:
- Herencia simple (clase vacía que hereda)
- Uso de super().__init__() para inicializar atributos del padre
- Agregar atributos propios a la clase hija

Corresponde a los slides 4-6 de la presentación.
"""


# ============================================================
# 1. Herencia simple — clase hija sin nada propio
# ============================================================

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")


# Estudiante HEREDA de Persona
class Estudiante(Persona):
    pass  # Por ahora no agregamos nada


# ============================================================
# 2. Agregar atributos propios con super()
# ============================================================

class EstudianteCompleto(Persona):
    def __init__(self, nombre, edad, carrera):
        # Llamar al __init__ del padre
        super().__init__(nombre, edad)
        # Agregar lo propio
        self.carrera = carrera


# ============================================================
# Pruebas
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("1. Herencia simple (sin atributos propios)")
    print("=" * 50)

    est = Estudiante("Ana", 20)
    print(f"Nombre: {est.nombre}")   # Ana — heredado de Persona
    print(f"Edad: {est.edad}")       # 20 — heredado de Persona
    est.saludar()                    # Funciona — heredado de Persona

    print()
    print("=" * 50)
    print("2. Herencia con super() y atributos propios")
    print("=" * 50)

    ana = EstudianteCompleto("Ana", 20, "Ingeniería")
    print(f"Nombre: {ana.nombre}")    # Ana — inicializado por el padre
    print(f"Edad: {ana.edad}")        # 20 — inicializado por el padre
    print(f"Carrera: {ana.carrera}")   # Ingeniería — inicializado por Estudiante
    ana.saludar()                     # Hola, soy Ana... — método heredado
