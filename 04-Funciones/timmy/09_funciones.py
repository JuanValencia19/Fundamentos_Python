'''
## 9️⃣ Mayor valor
Crea una función `mayor_valor(lista)` que retorne el número mayor sin usar max().
'''
import os
os.system("cls")

numeros = [2, 3, 5, 7, 8, 9, 3.1, 25, 10, 5, 1]

def mayor_valor(lista):
    numero = 0
    for item in numeros:
        if item >= numero:
            numero = item
        else:
            numero = numero
    return(numero)
    
print(f"Numero mayor de la lista: {mayor_valor(numeros)}")