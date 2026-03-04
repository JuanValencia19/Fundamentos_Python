'''
## 6️⃣ Ganancia de apuesta
Crea una función:

calcular_ganancia(monto, cuota, gano)

Si ganó → retorna monto * cuota
Si perdió → retorna 0
'''
import os
os.system("cls")

gano = True

def calcular_ganancia(monto, cuota, gano):
    if gano:
        return (f"Ganaste {monto * cuota}, felicidades")
    else:
        return ("No ganaste nadita")
    
resultado = calcular_ganancia(50000, 2.4, True)
print(resultado)

# Forma simple con operador ternario
# def calcular_ganancia(monto, cuota, gano):
#     return monto * cuota if gano else 0

'''
OPERADOR TERNARIO - EXPRESION CONDICIONAL

Forma tradicional
if edad >= 18:
    mensaje = "Mayor de edad"
else:
    mensaje = "Menor de edad"

Forma compacta
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
'''