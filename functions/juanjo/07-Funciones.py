#  7️⃣ Clasificador de cuota
# Crea una función `clasificar_cuota(cuota)` que retorne:

# - "Favorito" si cuota < 1.8
# - "Equilibrado" si está entre 1.8 y 2.5
# - "No favorito" si es mayor a 2.5

def clasificar_couta(couta):
    if couta < 1.8:
        return "Favorito"
    elif couta > 1.8 and couta <= 2.5:
        return "Equilibrado"
    elif couta > 2.5:
        return "No Favorito"

print(clasificar_couta(1.5))
print(clasificar_couta(2.3))
print(clasificar_couta(4.5))