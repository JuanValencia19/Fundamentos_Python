## 9️⃣ Sistema de apuesta robusto

# Crea un sistema que:

# - Pida monto
# - Pida cuota
# - Calcule ganancia

# Debe manejar:
# - Letras
# - División por cero
# - Cuotas inválidas

# El programa NO debe romperse nunca.

def calcular_ganancia(monto, cuota):
    while True:
        if cuota == 0:
            print("La cuota no debe ser igual a 0")
            cuota = float(input("Ingrese una cuota: "))
            break
    return monto * cuota
try:
    monto = float(input("Ingrese un monto: "))
    cuota = float(input("Ingrese una cuota: "))
    print(calcular_ganancia(monto, cuota))
except ValueError:
    print("Tipo entrada invalida, ingresa un numero flotante:")
except ZeroDivisionError:
    print("Estas dividiendo por 0")

