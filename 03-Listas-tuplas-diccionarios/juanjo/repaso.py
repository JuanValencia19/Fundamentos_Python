#🟢 PARTE 1 — LISTAS (8 ejercicios)
equipos = ["Real Madrid", "Manchester United", "Barcelona", "Arsenal", "PSG"]
print("Lista completa:", equipos)

#Ejercicio 2
print("Primer equipo:", equipos[0])
print("Último equipo:", equipos[-1])

#Ejercicio 3
equipos.append("Bayern Munich")
print(equipos)

#Ejercicio 4
equipos.remove("Barcelona")
print(equipos)

#Ejercicio 5
print(len(equipos))

#Ejercicio 6
for i in equipos:
    print(i)

#Ejercicio 7
cuotas = [1.80, 2.01, 6.50, 9.20, 4.00]
suma = 0
for cuota in cuotas:
    suma += cuota
print("Suma de cuotas:", suma)

#Ejercicio 8
mayor = cuotas[0]
for cuota in cuotas:
    if cuota > mayor:
        mayor = cuota
print("Cuota mayor:", mayor)

#🔵 PARTE 2 — TUPLAS (4 ejercicios)

#Ejercicio 9
partido = ("Real Madrid","Bayern Munich", 2, 1)
print(partido[0])
print(partido[1])
print(partido[2])
print(partido[3])

#Ejercicio 10
partido[1] = "Barcelona"   #tupple does not support item assignment
#Las tuplas son inmutables por lo que no se puede modificar un valor ya establecido

#Ejercicio 11
local, visitante, goles_local, goles_visitante = partido
print("Local:", local)
print("Visitante:", visitante)
print("Goles local:", goles_local)
print("Goles visitante:", goles_visitante)

#Ejercicio 12
if goles_local > goles_visitante:
    print("El equipo local gano el encuentro")
elif goles_visitante > goles_local:
    print("El equipo visitante ganó")
else:
    print("Partido en empate")

#🟣 PARTE 3 — DICCIONARIOS (8 ejercicios)
#Ejercicio 13

equipo = {
    "nombre": "Manchester United",  
    "pais": "Inglaterra",
    "titulos": 20
}
print(equipo["nombre"])
print(equipo["pais"])
print(equipo["titulos"])

#Ejercicio 14
equipo["estadio"] = "Old Trafford"
print(equipo)

#Ejercicio 15
equipo["titulos"] = 22

#Ejercicio 16
for clave, valor in equipo.items():
    print(f"La clave '{clave}' tiene el valor: {valor}")

#Ejercicio 17
coutas = {
    "local": 1.80,
    "empate": 3.40,
    "visitante": 4.20
}

implicita_local= 1 / coutas["local"]
implicita_empate= 1 / coutas["empate"]
implicita_visitante= 1 / coutas["visitante"]

print(f"la probabilidad implicita del local es: ${implicita_local}. El del visitante: ${implicita_visitante}. Y la del empate es de: ${implicita_empate}")

#Ejercicio 18

liga = {
    "equipo1": {"puntos": 45, "goles": 30},
    "equipo2": {"puntos": 50, "goles": 40}
}

print(liga["equipo1"]["puntos"])
print(liga["equipo2"]["puntos"])

#Ejercicio 19
consulta = input("Ingrese el nombre del equipo que quiere consultar")

liga1 = {
    "equipo1": {"nombre": "Real Madrid", "puntos": 60, "goles": 30},
    "equipo2": {"nombre": "Barcelona", "puntos": 61, "goles": 40}
}

for i in liga1.values():
    if consulta.lower() == i["nombre"].lower():
        print(i)
        break
    else: 
        print("Equipo no encontrado")
        resultados = ["local", "empate", "local", "visitante", "local"]

#Ejercicio 20
contador = {}

for i in resultados:
    if i in contador:
        contador[i] += 1
    else:
        contador[i] = 1
print(contador)