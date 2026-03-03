'''
## 5️⃣ Función par o impar
Crea una función `es_par(numero)` que retorne:
True si es par
False si es impar
'''
import os
os.system("cls")

def es_par(numero):
    if numero % 2 == 0:
        print("True")
    else:
        print("False")
        
es_par(23)