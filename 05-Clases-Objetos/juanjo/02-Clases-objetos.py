# ## 2️⃣ Método dentro de la clase

# Agrega un método llamado `presentarse()` que imprima:

# "Hola, soy [nombre] y juego como [posicion]"

# ---

class Jugador:
    def __init__(self, nombre, edad, posicion):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
    
    def presentarse(self):
        print(f"Hola soy {self.nombre} y juego como {self.posicion}")

jugador1 = Jugador("Courtois", 34, "Arquero")
jugador1.presentarse()