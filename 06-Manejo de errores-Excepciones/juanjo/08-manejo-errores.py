## 8️⃣ Lanzar excepción manual

# Crea una función `apostar(monto)`.

# Si el monto es mayor al saldo:
#     usa raise ValueError("Saldo insuficiente")

def apostar(monto):
        saldo = 975
        if monto > saldo and monto > 0:
            raise ValueError("Saldo insuficiente")
        print("APUESTA REALIZADA CORRECTAMENTE!")
try:
    resultado = apostar(1500)
except ValueError as error:
    print(error)