# 8️⃣ Clasificación de probabilidad implícita
# Pide una cuota decimal.
# Calcula probabilidad = 1 / cuota.

# Si probabilidad > 0.6 → Favorito claro
# Si entre 0.4 y 0.6 → Partido equilibrado
# Si menor a 0.4 → No favorito

couta_decimal = float(input("Ingresa tu couta en decimal: "))
probabilidad = 1 / couta_decimal

if probabilidad > 0.6:
    print("Favorito claro")
elif probabilidad >= 0.4 and probabilidad <= 0.6:
    print("Partido equilibrado")
elif probabilidad < 0.4:
    print("No favorito")