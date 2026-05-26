# 🔵 PARTE 2 — NIVEL INTERMEDIO (5 ejercicios)

## 6️⃣ Clase Partido

# Crea una clase `Partido` con:

# - local
# - visitante
# - goles_local
# - goles_visitante

# Agrega un método `resultado()` que retorne:
# - "Ganó local"
# - "Ganó visitante"
# - "Empate"

# ---

class Partido:
    def __init__(self, local, visitante, goles_local, goles_visitante):
        self.local = local
        self.visitante = visitante
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante
    def resultado(self):
        if self.goles_local > self.goles_visitante:
            return "Gano local"
        elif self.goles_local < self.goles_visitante:
            return "Gano Visitante"
        else:
            return "Empate"
partido1 = Partido("Real Madrid", "Atletico Madrid", 4, 1)
print(partido1.resultado())