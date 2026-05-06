'''
## 7️⃣ Clasificador de cuota
Crea una función `clasificar_cuota(cuota)` que retorne:

- "Favorito" si cuota < 1.8
- "Equilibrado" si está entre 1.8 y 2.5
- "No favorito" si es mayor a 2.5
'''

import os
os.system("cls")

cuota = 2.3

def clasificar_cuota(cuota):
    if cuota < 1.8:
        return ("Favorito")
    elif cuota <= 2.5:
        return ("Equilibrado")
    else:
        return ("No favorito")
    
resultado = clasificar_cuota(cuota)
print(resultado)