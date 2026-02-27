'''
## 9️⃣ Crear tupla
Crea una tupla con información de un partido:
(nombre_local, nombre_visitante, goles_local, goles_visitante)

Imprime cada dato por separado.
'''
import os
os.system("cls")

information_match = ("Manchester United", "Manchester City", 2, 0)

for i in information_match:
    print(i)
    
'''
## 🔟 Intentar modificar tupla
Intenta cambiar un valor de la tupla.
¿Qué ocurre? Explica en un comentario por qué.
'''

# information_match[1] = "Arsenal"
print(information_match)

# Porque las tuplas son inmutables, por lo tanto no se pueden modificar sus indices una vez creada la tupla

'''
## 1️⃣1️⃣ Desempaquetado
Desempaqueta la tupla en variables individuales:
local, visitante, goles_local, goles_visitante
'''

local, visitante, goles_local, goles_visitante = information_match
print(local, visitante, goles_local, goles_visitante)

'''
## 1️⃣2️⃣ Comparación de goles
Usando la tupla:
Determina quién ganó el partido usando condicionales.
'''

if goles_local == goles_visitante:
    print("Partido igualado")
elif goles_local > goles_visitante:
    print(f"Equipo ganador: {local}")
else:
    print(f"Equipo ganador: {visitante}")