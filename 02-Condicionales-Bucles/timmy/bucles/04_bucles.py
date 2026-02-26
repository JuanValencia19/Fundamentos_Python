'''
## 4️⃣ Contador regresivo
Pide un número y haz una cuenta regresiva hasta 0 usando while.
'''
import os
os.system("cls")

number = int(input("Ingresa un numero: "))

while number >= 0:
    print(number)
    number -= 1
    