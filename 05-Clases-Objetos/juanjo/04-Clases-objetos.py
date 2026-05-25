# ## 4️⃣ Modificar atributos

# Crea una clase `CuentaBancaria` con:

# - titular
# - saldo

# Crea un método `depositar(monto)` que aumente el saldo.

# Prueba depositando dinero.

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


cuenta1 = CuentaBancaria(
    "Juan",
    2000
)

monto_usuario = int(input(
    "Ingrese monto a depositar: "
))

cuenta1.depositar(monto_usuario)