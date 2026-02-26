'''
Pide la edad del usuario y muestra:
- "Mayor de edad" si tiene 18 o más
- "Menor de edad" si tiene menos de 18
'''
import os
os.system("cls")

age = int(input("Ingresa tu edad: "))

if age >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")