class SimuladorApuestas:
    def __init__(self, saldo):
        self.saldo = saldo
    def apostar(self, monto):
        self.saldo -= monto
        print(f"Apostaste {monto}")
    def mostrar_saldo(self):
        print(f"Tu saldo actual es: {self.saldo}")

apuesta1 = SimuladorApuestas(1000)
monto1 = float(input(
    "Ingrese la cantidad a apostar: "
))
apuesta1.apostar(monto1)
apuesta1.mostrar_saldo()
