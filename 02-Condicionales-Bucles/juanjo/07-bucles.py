# 7️⃣ Acumulador de apuestas
# Pide al usuario ingresar 5 cuotas.
# Guárdalas y calcula el promedio final.

suma = 0  # acumulador

for i in range(5):
    cuota = float(input(f"Ingrese la cuota {i+1}: "))
    suma += cuota  # acumulamos

promedio = suma / 5

print("El promedio final es:", promedio)

