# 8️⃣ Promedio de lista
# Crea una función `calcular_promedio(lista)` que reciba una lista de números y retorne el promedio.

# NO uses sum() ni len() (hazlo manual con bucle).

def calcular_promedio(lista):
    contador = 0
    suma = 0
    for i in lista:
        suma += i
        contador += 1
    return suma / contador

print(calcular_promedio([5,6,2,1]))
