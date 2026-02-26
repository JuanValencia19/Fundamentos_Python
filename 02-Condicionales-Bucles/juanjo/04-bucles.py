#  4️⃣ Contador regresivo
# Pide un número y haz una cuenta regresiva hasta 0 usando while.

num = int(input("Ingrese un numero para su cuenta regresiva: "))

while num > 0:
    print(f"Cuenta regresiva en: {num}")
    num -= 1
else:
    print("El numero es 0")
