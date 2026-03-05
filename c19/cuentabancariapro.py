class CuentaBancaria:
    def __init__(self, titular, saldo_inicial = 0):
        self._titular = titular
        self._saldo = saldo_inicial  # Atributo privado
        self._historial = []  # Lista para almacenar el historial de transacciones

        self._historial.append(f"Cuenta creada con saldo inicial de {saldo_inicial}")

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def historial(self):
        return self._historial.copy()
    
    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser mayor que cero.")

        self._saldo += cantidad
        self._historial.append(f"Depósito de {cantidad}. Saldo actual: {self._saldo}")
        print(f"Depósito exitoso. Saldo actual: {self._saldo}")

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que cero.")
        if cantidad > self._saldo:
            raise ValueError("Fondos insuficientes para realizar el retiro.")

        self._saldo -= cantidad
        self._historial.append(f"Retiro de {cantidad}. Saldo actual: {self._saldo}")
        print(f"Retiro exitoso. Saldo actual: {self._saldo}")

    def transferir(self, otra_cuenta, cantidad):
        self.retirar(cantidad)
        otra_cuenta.depositar(cantidad) 
        self._historial.append(f"Transferencia de {cantidad} a {otra_cuenta.titular}. Saldo actual: {self._saldo}")
        print(f"Transferencia exitosa. Saldo actual: {self._saldo}")

    if __name__ == "__main__":
        ana = CuentaBancaria("ana garcia", 1000)
        carlos = CuentaBancaria("carlos lopez", 500)

        ana.depositar(500)
        ana.retirar(200)
        ana.transferir(carlos, 300)

        print(f"\nSaldo Ana: {ana.saldo}")
        print(f"Saldo Carlos: {carlos.saldo}")

        print("\nHistorial de Ana:")
        for movimiento in ana.historial:
            print(f"\n{movimiento}")

        try:
            ana.saldo = 10000000
        except ValueError as e:
            print(f"x intento 1 fallo: {e}")

        try:
            ana.titular = "hacker"
        except AttributeError as e:
            print(f"x intento 2 fallo: {e}")

        try:            
            ana.retirar(-100)
        except ValueError as e:
            print(f"x intento 3 fallo: {e}")

        try:
            ana.retirar(99999999999999999999)
        except ValueError as e:
            print(f"x intento 4 fallo: {e}")

        histrorial_obtenido = ana.historial
        histrorial_obtenido.append("Movimiento no autorizado")
        print("\n se modifico el historial rean? no")
        print(f"ultimo movimiento real: {ana.historial[-1]}")
        