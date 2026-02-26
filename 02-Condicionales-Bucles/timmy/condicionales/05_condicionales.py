'''
Pide una nota del 0 al 100 y clasifica:
- 90–100 → Excelente
- 70–89 → Bueno
- 50–69 → Regular
- Menos de 50 → Reprobado
'''
import os
os.system("cls")

nota = float(input("Ingresa tu nota final: "))

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Bueno")
elif nota >= 50:
    print("Regular")
else:
    print("Reprobado")