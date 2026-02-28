#Las tuplas se definen con parentesis, son inmutables(por lo que no se pueden cambiar una vez definidas)
#Permite dupiclados y son ordenados


# 9️⃣ Crear tupla
# Crea una tupla con información de un partido:
# (nombre_local, nombre_visitante, goles_local, goles_visitante)

partido = ("Real Madrid", "Benfica", 2 , 1)

# 🔟 Intentar modificar tupla
# Intenta cambiar un valor de la tupla.
# ¿Qué ocurre? Explica en un comentario por qué.

# partido[1] = "Porto"
# print(partido)
#Error ya que las tuplas son inmutables


# 1️⃣1️⃣ Desempaquetado
# Desempaqueta la tupla en variables individuales:
# local, visitante, goles_local, goles_visitante

local = partido[0]
visitante = partido[1]
goles_local = partido[2]
goles_visitante = partido[3]

# 1️⃣2️⃣ Comparación de goles
# Usando la tupla:
# Determina quién ganó el partido usando condicionales.

if partido[2] > partido[3]:
    print("El local gano el partido")
elif partido[2] == partido[3]:
    print("Partido en empate")
else:
    print("Gano el equipo visitante")
