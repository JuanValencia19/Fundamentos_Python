# 6️⃣ Simulación de banca
# Empieza con saldo = 1000

# Mientras el saldo sea mayor que 0:
# - Resta 100
# - Imprime el saldo actual

# Cuando llegue a 0, imprime "Sin fondos"

saldo = 1000
while saldo > 0:
    saldo = saldo - 100
    print(saldo)
else:
    print("Sin fondos")
