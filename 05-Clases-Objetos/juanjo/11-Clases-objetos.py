## 1️⃣1️⃣ Clase Equipo con estadísticas

# Crea una clase `Equipo` con:

# - nombre
# - goles_a_favor
# - goles_en_contra

# Agrega un método que calcule diferencia de gol.

class Equipo:
    def __init__(self, nombre, goles_a_favor, goles_en_contra):
        self.nombre = nombre
        self.goles_a_favor = goles_a_favor
        self.goles_en_contra = goles_en_contra
    ## 1️⃣1️⃣ Clase Equipo con estadísticas

# Crea una clase `Equipo` con:

# - nombre
# - goles_a_favor
# - goles_en_contra

# Agrega un método que calcule diferencia de gol.

class Equipo:
    def __init__(self, nombre, goles_a_favor, goles_en_contra):
        self.nombre = nombre
        self.goles_a_favor = goles_a_favor
        self.goles_en_contra = goles_en_contra
    def diferencia_gol(self):
        return self.goles_a_favor - self.goles_en_contra
equipo1 = Equipo("Real Madrid", 70, 35)
print(equipo1.diferenciaGol())