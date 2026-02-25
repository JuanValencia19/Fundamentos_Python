'''
Pide una cuota decimal.
Calcula probabilidad = 1 / cuota.

Si probabilidad > 0.6 → Favorito claro
Si entre 0.4 y 0.6 → Partido equilibrado
Si menor a 0.4 → No favorito
'''

import os
os.system("cls")

cuota = float(input("Escribe tu cuota: "))

while cuota <= 0 and cuota >= 1:
    print("Cuota incorrecta.")
    cuota = float(input("Ingresa nuevamente tu cuota: "))

cuota_calculo = 1 / cuota

if cuota_calculo >= 0.6:
    print("Favorito claro")
elif cuota_calculo >= 0.4:
    print("Partido equilibrado")
else:
    print("No favorito")