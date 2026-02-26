'''
## 1️⃣ Número positivo, negativo o cero
Pide un número al usuario y determina si es:
- Positivo
- Negativo
- Cero
'''

import os
os.system("cls")

number = float(input("Ingresa un numero: "))

if number == 0:
    print("Es igual a Cero")
elif number > 0: 
    print("Mayor que Cero, numero positivo")
else:
    print("Menor que Cero, numero negativo")