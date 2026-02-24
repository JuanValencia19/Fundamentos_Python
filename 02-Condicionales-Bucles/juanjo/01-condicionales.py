# 1️⃣ Número positivo, negativo o cero
# Pide un número al usuario y determina si es:
# - Positivo
# - Negativo
# - Cero

num = int(input("Ingrese un numero entero: "))

if num == 0:
    print("El numero es 0")
elif num < 0:
    print("El numero es negativo")
else:
    print("El numero es positivo")