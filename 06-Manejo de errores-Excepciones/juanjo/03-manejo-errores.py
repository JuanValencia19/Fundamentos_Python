# Pide al usuario:
# - Monto
# - Cuota

# Captura:
# - ValueError
# - ZeroDivisionError

# Muestra un mensaje diferente para cada error.

try:
    monto = float(input("Ingresa el monto: "))
    couta = float(input("Ingresa la couta: "))
except ValueError:
    print("Error en el valor ingresado")
except ZeroDivisionError:
    print("Error al dividir por 0")