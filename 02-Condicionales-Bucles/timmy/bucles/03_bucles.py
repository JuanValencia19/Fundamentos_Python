'''
## 3️⃣ Tabla de multiplicar
Pide un número y muestra su tabla del 1 al 10.
'''
import os
os.system("cls")

number = int(input("Ingresa un numero, para mostrar su tabla de multiplicar: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")