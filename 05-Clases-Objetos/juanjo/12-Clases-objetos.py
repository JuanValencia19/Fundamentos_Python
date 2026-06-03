## 1️⃣2️⃣ Historial de partidos

# Haz que la clase `Equipo` tenga una lista interna llamada `historial`.

# Crea un método `agregar_partido(partido)`.

class Equipo:

    def __init__(
        self,
        nombre,
        goles_a_favor,
        goles_en_contra
    ):
        self.nombre = nombre
        self.goles_a_favor = goles_a_favor
        self.goles_en_contra = goles_en_contra
        self.historial = []
    def agregar_partido(self, partido):
        self.historial.append(partido)