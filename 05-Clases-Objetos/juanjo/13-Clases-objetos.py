## 1️⃣3️⃣ Simulación básica

# Crea una clase `SimuladorTemporada` que:

# - Reciba una lista de equipos
# - Permita simular partidos
# - Actualice estadísticas

# (No necesitas hacerlo complejo, solo lógica básica)


class Equipo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.goles_a_favor = 0
        self.goles_en_contra = 0
        self.historial = []

    def mostrar_estadisticas(self):
        print(f"\nEquipo: {self.nombre}")
        print(f"Goles a favor: {self.goles_a_favor}")
        print(f"Goles en contra: {self.goles_en_contra}")


class Partido:

    def __init__(
        self,
        local,
        visitante,
        goles_local,
        goles_visitante
    ):
        self.local = local
        self.visitante = visitante
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante

    def resultado(self):
        return (
            f"{self.local.nombre} "
            f"{self.goles_local} - "
            f"{self.goles_visitante} "
            f"{self.visitante.nombre}"
        )


class SimuladorTemporada:

    def __init__(self, equipos):
        self.equipos = equipos
        self.partidos = []

    def simular_partido(
        self,
        local,
        visitante,
        goles_local,
        goles_visitante
    ):

        partido = Partido(
            local,
            visitante,
            goles_local,
            goles_visitante
        )

        self.partidos.append(partido)

        # Actualizar estadísticas local
        local.goles_a_favor += goles_local
        local.goles_en_contra += goles_visitante

        # Actualizar estadísticas visitante
        visitante.goles_a_favor += goles_visitante
        visitante.goles_en_contra += goles_local

        # Guardar historial
        local.historial.append(
            partido.resultado()
        )

        visitante.historial.append(
            partido.resultado()
        )

        print("Partido registrado:")
        print(partido.resultado())