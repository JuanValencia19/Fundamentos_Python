# ## 3️⃣ Clase Equipo

# Crea una clase `Equipo` con:

# - nombre
# - pais
# - titulos

# Crea dos equipos diferentes e imprime su información.

class Equipo:
    """Representa a un equipo de fútbol."""

    def __init__(self, nombre, pais, titulos):
        self.nombre = nombre
        self.pais = pais
        self.titulos = titulos

equipo1 = Equipo("Real Madrid", "Espana", 105)
equipo2 = Equipo("Manchester United", "Inglaterra", 68)

print(f"Info equipo1: {equipo1.nombre} , {equipo1.pais} , {equipo1.titulos} titulos")
print(f"Info equipo2: {equipo2.nombre} , {equipo2.pais} , {equipo2.titulos} titulos")