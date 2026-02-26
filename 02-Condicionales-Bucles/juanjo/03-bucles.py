# 3️⃣ Tabla de multiplicar
# Pide un número y muestra su tabla del 1 al 10.
num = int(input("Ingresa un numero natural para ver su tabla de multiplicar: "))

for i in range(1,11):
    multiplicador = i * num
    print(f"La multiplicacion es: {num} x {i} = {multiplicador}")