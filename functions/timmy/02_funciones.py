'''
## 2️⃣ Función con parámetro
Crea una función `saludar_usuario(nombre)` que imprima:
"Hola, [nombre]"

Llama la función pasando tu nombre.
'''
import os
os.system("cls")

def saludar_usuario(nombre):
    print(f"Hola, {nombre}")

saludar_usuario("Timmy")