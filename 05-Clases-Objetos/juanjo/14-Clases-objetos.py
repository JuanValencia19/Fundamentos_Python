## 1️⃣4️⃣ Mini sistema completo

# Crea:

# - Clase `Equipo`
# - Clase `Partido`
# - Clase `Apuesta`

# Haz que trabajen juntas en un pequeño flujo:

# 1. Se crea un partido
# 2. Se hace una apuesta
# 3. Se muestra el resultado
# 4. Se calcula la ganancia

class Equipo:
    def __init__(self, nombre, goles_a_favor, goles_en_contra):
        self.nombre = nombre
        self.goles_a_favor = goles_a_favor
        self.goles_en_contra = goles_en_contra
class Partido:
    def __init__(
    self,
    equipo_local,
    equipo_visitante,
    goles_local,
    goles_visitante
):
        self.equipo_visitante = equipo_visitante
        self.equipo_local = equipo_local
        self.goles_visitante = goles_visitante
        self.goles_local = goles_local
    def resultado(self):
        return (
            f"{self.equipo_local.nombre} "
            f"{self.goles_local} - "
            f"{self.goles_visitante} "
            f"{self.equipo_visitante.nombre}"
        )
    def ganador(self):
        if self.goles_local > self.goles_visitante:
            return self.equipo_local
        elif self.goles_local < self.goles_visitante:
            return self.equipo_visitante
        else:
            return "Empate"
class Apuesta:
    def __init__(self, equipo_apostado, cantidad_apostada, cuota):
        self.equipo_apostado = equipo_apostado
        self.cantidad_apostada = cantidad_apostada
        self.couta = cuota
    def ganancia(self, partido):
        if partido.ganador() == self.equipo_apostado:
            ganacia = self.cantidad_apostada * self.couta
            return f"¡Apuesta Ganadora! Haz ganado: {ganacia}"
        else:
            return "Apuesta perdida"

real_madrid = Equipo("Real Madrid", 70, 35)
barcelona = Equipo("Barcelona", 80, 42)
partido = Partido(
    real_madrid,
    barcelona,
    3,
    1
)
apuesta = Apuesta(
    real_madrid,
    10000,
    1.80
)

print(partido.resultado())

print(
    f"Ganancia: {apuesta.ganancia(partido)}"
)