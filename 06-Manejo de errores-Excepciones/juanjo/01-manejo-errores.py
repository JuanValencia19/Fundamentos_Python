## 1️⃣ Error de división

# Pide dos números al usuario.
# Haz una división.

# Si el usuario intenta dividir por 0:
#     muestra "No se puede dividir por cero"

num1 = float(input("Ingresa un numero para dividir: "))

num2 = float(input("Ingresa un numero para dividir: "))

try:
    print(num1 / num2)
except:
    print("Se ha producido un error al dividir por cero")
