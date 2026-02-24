#  6️⃣ Apuesta ganadora
# Pide:
# - Cuota decimal
# - Resultado (1 si ganó, 0 si perdió)

# Si ganó:
#     calcula ganancia = 100 * cuota
# Si perdió:
#     muestra "Apuesta perdida"

couta_decimal = float(input("Ingresa la couta decimal de la apuesta: "))

resultado = int(input("Ingresa 1 si la apuesta se gano o ingesa 0 si perdiste: "))
ganancia = 100*couta_decimal

if resultado == 1:
    print("Total ganancia es: ", ganancia)
else:
    print("Apuesta perdida")
