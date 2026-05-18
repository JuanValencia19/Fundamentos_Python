#Ejercicio 1
determinar_numero = int(input("Pasa un numero entero positivo, negativo o 0: "))

if determinar_numero > 0:
    print("El numero es positivo")
elif determinar_numero < 0:
    print("El numero es negativo")
else:
    print("El numero es 0")

#Ejercicio 2
par_impar = int(input("Ingresa un numero entero: "))

if par_impar % 2 == 0:
    print("Numero es par")
else:
    print("Numero impar") 

#Ejercicio 3
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Ejercicio 4
numero1 = input("Ingresa un numero cualquiera")
numero2 = input("Ingresa otro numero para comparacion")

if numero1 > numero2:
    print("El primer numero es el mayor")
elif numero1 < numero2:
    print("El segundo numero ingresado es el mayor")
else:
    print("Los dos numeros son iguales")

#Ejercicio 5
nota = int(input("Ingresa la nota del estudiante del 0 al 100"))

if nota > 89 and nota <= 100:
    print("Excelente")
elif nota > 69 and nota <= 89:
    print("Bueno")
elif nota > 49 and nota <= 69:
    print("Regular")
elif nota < 49:
    print("Reprobado")
else:
    print("Numero no valido") 

#Ejercicio 6
couta_decimal = float(input("Ingresa el numero de la couta en decimal: "))
resultado = int(input("Ingresa 1 si ganaste la apuesta o 0 si perdiste para calcular la ganancia"))

if resultado == 1:
    print("gano: " + 100 * couta_decimal)
elif resultado == 0:
    print("Apuesta perdida")
elif resultado != 0 and resultado != 1:
    print("Ingrese un numero valido 1 o 0")


#Ejercicio 7
contrasena = "juanchitovt123"
revision = input("Ingresa la llave secreta: ")
if revision == contrasena:
    print("Felicidades. Acceso concedido")
else: 
    print("Acceso denegado")

# 🔵 PARTE 2 — BUCLES (8 ejercicios)

#Ejercicio 1
for i in range(11):
    print(i)

#Ejercicio 2
contador = 0
for i in range(101):
    contador += i
print(contador)

#Ejercicio 3
tabla_mult = int(input("Ingrese un numero para conocer su tabla de multiplicar: "))
count = 0
while count < 10:
    print(tabla_mult * count)
    count += 1

#Ejercicio 4
num_while = int(input("Ingresa un numero para ver su cuenta regresiva: "))
while num_while > 0:
    num_while -= 1
    print("La cuenta regresiva: ", num_while)

#Ejercicio 5
for i in range(51):
    if i % 2 == 0:
        print(i)

#Ejercicio 6
saldo = 1000
while saldo > 0:
    saldo -= 100
    print(saldo)
    if saldo == 0:
        print("Fondos insuficientes")

#Ejercicio 7

suma = 0
for i in range(4):
    couta = input("Ingrese la cantidad de la couta: ")
    suma += couta

promedio = suma / 5
print("El promedio es: ", promedio)

#Ejercicio 8
while True:
    contador = int(input("Ingrese un numero entero cualquiera o 0 para finalizar:"))
    if contador == 0:
        print("Programa finalizado")
        break



