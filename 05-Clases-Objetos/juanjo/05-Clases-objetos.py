# ## 5️⃣ Método condicional

# En `CuentaBancaria`, crea un método `retirar(monto)`:

# - Si hay saldo suficiente → resta el monto
# - Si no → imprime "Fondos insuficientes"

# ---
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
    def retirar(self,retiro):
        if self.saldo < retiro:
            print("Retiro mayor que saldo. Fondos insuficientes")
        else:
            self.saldo -= retiro
            print(f"Su nuevo saldo es: {self.saldo}")

cuenta1 = CuentaBancaria(
    "Juan",
    2000
)

monto_deposito = int(input(
    "Ingrese monto a depositar: "
))

monto_retiro = int(input("Ingrese monto a retirar: "))

cuenta1.depositar(monto_deposito)
cuenta1.retirar(monto_retiro)
