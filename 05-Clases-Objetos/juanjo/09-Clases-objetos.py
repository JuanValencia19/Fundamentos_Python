## 9️⃣ Lista de objetos

# Crea 3 objetos `Partido` y guárdalos en una lista.

# Recorre la lista y muestra el resultado de cada partido usando el método `resultado()`.

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

partido2 = Partido("Manchester United", "Chelsea", 1, 1)

partido3 = Partido("Real Madrid", "Liverpool", 3, 1)

partidos = [
    partido1,
    partido2,
    partido3
]

for partido in partidos:

    print(partido.resultado())

