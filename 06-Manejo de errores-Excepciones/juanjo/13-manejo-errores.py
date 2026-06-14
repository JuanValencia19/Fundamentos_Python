## 1️⃣3️⃣ Simulador seguro

# Crea una clase SimuladorApuestas que:

# - Maneje errores si el usuario mete texto
# - No permita apostar más del saldo
# - Siempre continúe ejecutándose

class SimuladorApuestas:
    def __init__(self, saldo):
        self.saldo = saldo
        if not isinstance(self.saldo, (int, float)):
            raise ValueError("El saldo debe ser un número")
    def apostar(self, monto):
        if monto <= 0:
            raise ValueError("No se permite apostar 0 o un numero negativo")
        if monto > self.saldo:
            raise ValueError("No se puede apostar un monto mayor al saldo")
        
        self.saldo -= monto
        print(f"Apostaste {monto}")
    def mostrar_saldo(self):
        print(f"Tu saldo actual es: {self.saldo}")

obj1 = SimuladorApuestas(1000)
while True:
    try:
        apuesta = float(input("Ingresa el monto a apostar: "))
        if apuesta == 0:
            break
        obj1.apostar(apuesta)
        obj1.mostrar_saldo()
    except ValueError as error:
            print(error)