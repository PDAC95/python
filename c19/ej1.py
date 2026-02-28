class Ejemplo:
    def __init__(self):
      self.publico = "Valor público"
      self._privado = "Valor privado"
      self.__muy_privado = "no me toques soy muy privado"
    
    
obj = Ejemplo()
print(obj.publico)  # Acceso directo al atributo público
print(obj._privado)  # Acceso directo al atributo privado (no recomendado)  
print(obj._Ejemplo__muy_privado)  # Acceso al atributo muy privado (no recomendado)