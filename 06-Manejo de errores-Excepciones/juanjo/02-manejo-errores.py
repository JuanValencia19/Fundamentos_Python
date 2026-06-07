## 2️⃣ Validar número entero

# Pide al usuario un número.
# Si escribe algo que no sea número:
#     muestra "Entrada inválida"

try:
    numero = int(input("Ingresa un número: "))
except ValueError:
    print("Entrada inválida")