'''
## 1️⃣7️⃣ Diccionario de cuotas
Crea un diccionario:
{
    "local": 1.80,
    "empate": 3.40,
    "visitante": 4.20
}

Calcula la probabilidad implícita de cada resultado (1/cuota).
'''
import os
os.system("cls")

cuota = {
    "local": 1.80,
    "empate": 3.40,
    "visitante": 4.20
}

for clave, valor in cuota.items():
    print(f"{clave}: Probabilidad implicita: {round((1 / valor) * 100, 2)}")