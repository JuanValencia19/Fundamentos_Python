'''
## 8️⃣ Promedio de lista
Crea una función `calcular_promedio(lista)` que reciba una lista de números y retorne el promedio.

NO uses sum() ni len() (hazlo manual con bucle).
'''
import os
os.system("cls")

numeros = [2, 3, 5, 7, 8, 9, 3.1, 25, 10]

def calcular_promedio(lista):
    
    sumar = 0
    contador = 0

    for i in numeros:
        print(i)
        sumar += i
        contador += 1
    return (f"Promedio {round(sumar / contador, 2)}")
    
resultado = calcular_promedio(numeros)
print(resultado)