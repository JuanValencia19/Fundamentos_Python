# 6️⃣ Ganancia de apuesta
# Crea una función:

# calcular_ganancia(monto, cuota, gano)

# Si ganó → retorna monto * cuota
# Si perdió → retorna 0

def  calcular_ganancia(monto, couta, gano):
    if gano == True:
        return monto * couta
    else: 
        return 0
print(calcular_ganancia(1400, 2.30, True))
print(calcular_ganancia(1400, 2.30, False))