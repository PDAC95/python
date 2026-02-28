class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    @property
    def saldo(self):
        """getter para el saldo"""
        return self.__saldo
    @saldo.setter
    def saldo(self, valor):
        """setter para el saldo"""
        if valor < 0:
            print("No se puede establecer un saldo negativo.")
        else:
            self.__saldo = valor
            print(f"saldo actualizado a {self.__saldo}")

cuenta = CuentaBancaria("Juan Pérez", 1000)
print(cuenta.titular)  # Acceso al atributo público

cuenta.saldo = 5000
print(cuenta.saldo)  # Acceso al saldo a través del getter

cuenta.saldo = -100  # Intento de establecer un saldo negativo
print(cuenta.saldo)  # El saldo no se actualiza debido a la validación