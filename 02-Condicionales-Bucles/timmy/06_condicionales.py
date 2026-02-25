'''
Pide:
- Cuota decimal
- Resultado (1 si ganó, 0 si perdió)

Si ganó:
    calcula ganancia = 100 * cuota
Si perdió:
    muestra "Apuesta perdida"
'''

import os
os.system("cls")

cuota = float(input("Cuotas\n1. Gano\n0. Perdio\nEscribe tu cuota: "))

while cuota != 0 and cuota != 1:
    print("Valor incorrecto, ingresa un numero correcto")
    cuota = float(input("Cuotas\n1. Gano\n0. Perdio\nEscribe tu cuota: "))
    
if cuota == 1:
    print(f"Resultado final: {100 * cuota}")
else:
    print("Apuesta perdida")
    