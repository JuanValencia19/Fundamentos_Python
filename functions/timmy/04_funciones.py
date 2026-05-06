'''
## 4️⃣ Función para calcular cuota
Crea una función `probabilidad(cuota)` que retorne:

1 / cuota

Muestra el resultado.
'''
import os
os.system("cls")

def probabilidad(cuota):
    return round(1 / cuota, 2)

print(probabilidad(2.3))