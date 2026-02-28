class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.tiular = titular
        self.saldo = saldo

    def depositar(self, cantindad):
        self.saldo += cantindad
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("No tienes suficiente saldo para retirar esa cantidad.")
        else:
            self.saldo -= cantidad

cuenta_claudio = CuentaBancaria("Claudio", 10000) #1 
print(cuenta_claudio.saldo)

cuenta_claudio.depositar(500) #2
print(cuenta_claudio.saldo)

cuenta_claudio.retirar(200) #3
print(cuenta_claudio.saldo) 

cuenta_claudio.retirar(20000)   #4 
print(cuenta_claudio.saldo) #saldo no cambia porque no se pudo retirar la cantidad solicitada.

cuenta_nestor = CuentaBancaria("Nestor", 5000) #av siempre viva 44
cuenta_emmanuel = CuentaBancaria("Emmanuel", 2000) #av siempre viva 45
cuenta_yan=CuentaBancaria("Yan", 3000) #av siempre viva 46
cuenta_arturo=CuentaBancaria("Arturo", 4000) #av siempre viva 47
cuenta_ricardo=CuentaBancaria("Ricardo", 6000) #av siempre viva 48
