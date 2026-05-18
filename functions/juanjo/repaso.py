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

