## 7️⃣ Clase Apuesta

# Crea una clase `Apuesta` con:

# - monto
# - cuota
# - gano (True/False)

# Agrega un método `calcular_ganancia()` que:

# - Retorne monto * cuota si ganó
# - Retorne 0 si perdió

# ---

class Apuesta:
    def __init__(self, monto, couta, gano):
        self.monto = monto
        self.couta = couta
        self.gano = gano
    def calcular_ganancia(self):
        if self.gano == True:
            return self.monto * self.couta
        else:
            return 0
apuesta1 = Apuesta(400, 1.90, True)
print(apuesta1.calcular_ganancia())