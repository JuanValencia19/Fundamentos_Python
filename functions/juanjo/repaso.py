# 🟢 PARTE 1 — FUNDAMENTOS (5 ejercicios)
def saludar():
    print("Bienvenido al sistema de analisis deportivos")
saludar()

#Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}")
saludar_usuario("Juanchitovt")

#Ejercicio 3
def sumar(a,b):
    return a + b
resultado = sumar(5,7)
print(resultado)

#Ejercicio 4
def probabilidad(couta):
    return 1 / couta
apuesta = probabilidad(4.90)
print(apuesta)

#Ejercicio 5
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
par = es_par(8)
print(par)

# 🔵 PARTE 2 — FUNCIONES CON LÓGICA (6 ejercicios)

#Ejercicio 6
def calcular_ganancia(monto, couta, gano):
    if gano == True:
        return monto * couta
    else:
        return 0
ganancia = calcular_ganancia(550,1.90,True)
print(ganancia)

#Ejercicio 7
def clasificar_couta(couta):
    if couta < 1.8:
        return "Favorito"
    elif couta >= 1.8 and couta <= 2.5:
        return "Equilibrado"
    elif couta > 2.5:
        return "No favorito"
couta1 = clasificar_couta(2.4)
print(couta1)

#Ejercicio 8
def calcular_promedio(lista):
    contador = 0
    promediador = 0
    for i in lista:
        contador += i
        promediador += 1
    promedio = contador / promediador
    return promedio
calculo1 = calcular_promedio([5,7,2,9,4,20])
print(calculo1)

#Ejercicio 9
def mayor_valor(lista):
    mayor = lista[0]
    for i in lista:
        if mayor < i:
            mayor = i
    return mayor
valores = mayor_valor([1.20,8.70,16.5,11.0,23.4,7.50,2.60])
print(valores)

#Ejercicio 10
def conteo_dic(lista):
    contador = {}
    for i in lista:
        if i in contador:
            contador[i] += 1
        else:
            contador[i] = 1
    return contador
conteo = conteo_dic(["local", "empate", "local", "visitante"])
print(conteo)

#Ejercicio 11

def probabilidad(cuota):
    return 1 / cuota

def valor_esperado(monto, cuota, prob_real):
    return (monto * cuota) * prob_real

prob_real = probabilidad(1.50)

valor1 = valor_esperado(
    800,
    1.50,
    prob_real
)

print(valor1)

#Ejercicio 12
def goles(goles_local, goles_visitante):
    if goles_local > goles_visitante:
        return "Local gano"
    elif goles_local < goles_visitante:
        return "Visitante gano"
    else:
        return "Empate"
partido = goles(4,3)
print(partido)

#Ejercicio 13
def simulador_apuestas(lista):
    combinada = 0
    for i in lista:
        combinada += i
        ganancia_total += combinada + 100
    return ganancia_total
apuesta = simulador_apuestas([1.90,2.05,1.14,7.0,3.3])

#Ejercicio 14
def pedir_cuota():
    while True:
        cuota = float(input("Ingrese la cuota: "))
        if cuota > 1:
            print("Cuota válida")
            break
        else:
            print("Cuota no válida")
pedir_cuota()  

#Ejercicio 15
def pedir_datos():
    cuota = float(input("Ingrese una cuota decimal: "))
    return cuota
def calcular_probabilidad(cuota):
    probabilidad = 1 / cuota
    return probabilidad
def mostrar_resultado(resultado):
    print(f"La probabilidad es: {resultado}")

cuota_usuario = pedir_datos()
resultado = calcular_probabilidad(cuota_usuario)
mostrar_resultado(resultado)
