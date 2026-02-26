'''
## 7️⃣ Acumulador de apuestas
Pide al usuario ingresar 5 cuotas.
Guárdalas y calcula el promedio final.
'''
import os
os.system("cls")

cuotas = []

while len(cuotas) <= 4:
    cuota_user = float(input("Ingresa una cuota: "))
    cuotas.append(cuota_user)
    
print(f"Promedio final: {sum(cuotas) / len(cuotas)}")
    