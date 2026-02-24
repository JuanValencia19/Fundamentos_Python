# 4️⃣ Comparación de dos números
# Pide dos números y muestra:
# - Cuál es mayor
# - O si son iguales

num1 = int(input("Ingresa un numero entero: "))
num2 = int(input("Ingresa otro numero entero para comparacion: "))

if num1 > num2:
    print("El numero 1 es mayor y el numero 2 menor")
elif num1 < num2:
    print("El numero 2 es mayor y numero 1 menor")
else:
    print("Ambos numero son iguales")
    