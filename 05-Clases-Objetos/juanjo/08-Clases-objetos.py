## 8️⃣ Contador interno

# Crea una clase `SimuladorApuestas` que tenga:

# - saldo inicial
# - método para apostar
# - método para mostrar saldo

# Cada apuesta debe modificar el saldo.

class SimuladorApuestas:
    def __init__(self, saldo):
        self.saldo = saldo
    def apostar(self, monto):
        return self.saldo - monto
    def mostrarsaldo(self):
        return self.saldo

monto1 = input("Ingrese la cantidad a apostar: ")
apuesta1 = SimuladorApuestas(1000)
print(apuesta1(monto1))