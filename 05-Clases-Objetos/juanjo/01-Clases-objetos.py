# 🟢 PARTE 1 — FUNDAMENTOS (5 ejercicios)
# Crea una clase llamada `Jugador`.

# Debe tener:
# - nombre
# - edad
# - posicion

# Crea un objeto e imprime sus atributos.

class Jugador:

    def __init__(self, nombre, edad, posicion):

        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion


juan = Jugador("Juan", 20, "Mediocampista")

print(juan.nombre)
print(juan.edad)
print(juan.posicion)