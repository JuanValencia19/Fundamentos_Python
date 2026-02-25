'''
Pide dos números y muestra:
- Cuál es mayor
- O si son iguales
'''

import os
os.system("cls")

number1 = int(input("Ingresa un numero: "))
number2 = int(input("Ingresa otro numero: "))

if number1 == number2:
    print("Son numeros iguales")
elif number1 > number2:
    print(f"{number1} es mayor que {number2}")
else:
    print(f"{number2} es mayor que {number1}")