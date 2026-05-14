'''
## 3️⃣ Función suma
Crea una función `sumar(a, b)` que retorne la suma.
Imprime el resultado al llamarla.
'''
import os 
os.system("cls")

def sumar(number_one: int, number_two: int):
    resultado = number_one + number_two
    return resultado

print(sumar(10, 2))