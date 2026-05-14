'''
## 🔟 Contador de resultados

Crea una función que reciba una lista como:
["local", "empate", "local", "visitante"]

Y retorne un diccionario con el conteo.
'''

import os
os.system("cls")

listado = {}
lista = ["local", "empate", "local", "visitante", "local", "empate", "local"]

def contar_tipos(lista):
    for item in lista:
        if item in listado:
            listado[item] += 1
        else:
            listado[item] = 1
    print(listado)

contar_tipos(lista)