'''
## 8️⃣ Bucle con break
Pide números al usuario continuamente.
Si el usuario escribe 0:
    termina el programa usando break.
'''
import os
os.system("cls")

number = int(input("Ingresa un numero: "))

while number != 0:
    number = int(input("Ingresa un numero: "))