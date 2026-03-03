'''
## 2️⃣0️⃣ Contador de resultados
Crea una lista con resultados:
["local", "empate", "local", "visitante", "local"]

Cuenta cuántas veces aparece cada resultado usando un diccionario.
'''
import os
os.system("cls")

repeticiones = {}

resultados = ["local", "empate", "local", "visitante", "local"]

for i in resultados:
    if i in repeticiones:
        repeticiones[i] += 1
    else:
        repeticiones[i] = 1
        
print(repeticiones)