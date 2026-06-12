## 1️⃣2️⃣ Clase con manejo de errores

# Modifica tu clase CuentaBancaria:

# En retirar():
#     si saldo insuficiente → raise Exception

# Maneja el error al usar el método.
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Nuevo saldo: {self.saldo}")
        else:
            print("Monto inválido")
    def retirar(self, retiro):
        if retiro > self.saldo:
            raise ValueError("El retiro es mayor que tu saldo")
        else:
            self.saldo -= retiro
            print(f"Nuevo saldo: {self.saldo}")

cuenta1 = CuentaBancaria(
    "Juan",
    2000
)

monto_usuario = int(input(
    "Ingrese monto a depositar: "
))

cuenta1.depositar(monto_usuario)

try:
    cuenta1.retirar(3000)
except ValueError as error:
    print(error)