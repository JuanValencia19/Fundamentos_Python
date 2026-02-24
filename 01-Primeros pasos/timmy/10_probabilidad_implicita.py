'''Pide al usuario:

- Una cuota decimal

Calcula:

probabilidad = 1 / cuota

Imprime el resultado en formato decimal y en porcentaje.
'''

import os
os.system("cls")

cuota = float(input("Ingresa el valor de la cuota: "))
formula_final = ((1 / cuota) * 100)
print(f"La probabilidad implicita con una cuota de {cuota} es de {round(formula_final, 2)}")