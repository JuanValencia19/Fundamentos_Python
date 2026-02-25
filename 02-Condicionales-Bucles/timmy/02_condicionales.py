'''
## 2️⃣ Número par o impar
Pide un número entero y determina si es par o impar.
'''
import os
os.system("cls")

number = int(input("Ingresa un numero: "))

if number % 2 == 0:
    print("Numero Par.")
else:
    print("Numero Impar")