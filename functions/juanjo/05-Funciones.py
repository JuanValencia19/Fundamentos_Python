# 5️⃣ Función par o impar
# Crea una función `es_par(numero)` que retorne:
# True si es par
# False si es impar

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(8))
