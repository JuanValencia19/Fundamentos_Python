# Los diccionarios se utilizan para almacenar valores en pares: clave y valor
# Un diccionario es una coleccion ordenada, modificable y no permite duplicados y son mutables
# 1️⃣3️⃣ Crear diccionario
# Crea un diccionario que represente un equipo:
equipo = {
    "nombre": "Real Madrid",
    "pais": "España",
    "titulos": 36
}

# Imprime cada valor usando su clave.

print(equipo["nombre"])
print(equipo["pais"])
print(equipo["titulos"])

# 1️⃣4️⃣ Agregar clave
# Agrega una nueva clave llamada "estadio".

equipo["estadio"] = "Santiago Bernabeu"

# 1️⃣5️⃣ Modificar valor
# Cambia el número de títulos.

equipo.update({"titulos": 106})
print(equipo)
# 1️⃣6️⃣ Recorrer diccionario
# Imprime todas las claves y valores usando un bucle for.

for i in equipo:
    print(equipo[i])

# 1️⃣7️⃣ Diccionario de cuotas
# Crea un diccionario:
couta = {
     "local": 1.80,
     "empate": 3.40,
     "visitante": 4.20
}

# Calcula la probabilidad implícita de cada resultado (1/cuota).

probabilidad_implicita = 1 / couta["local"]
probabilidad_implicita1 = 1 / couta["empate"]
probabilidad_implicita2 = 1 / couta["visitante"]
print(probabilidad_implicita)
print(probabilidad_implicita1)
print(probabilidad_implicita2)

# 1️⃣8️⃣ Diccionario anidado
# Crea un diccionario con varios equipos:

liga = {
    "equipo1": {"nombre": "Real Madrid", "puntos": 60, "goles": 30},
    "equipo2": {"nombre": "Barcelona", "puntos": 61, "goles": 40}
}

# Imprime los puntos de cada equipo.

print(liga["equipo1"]["puntos"])
print(liga["equipo2"]["puntos"])

# 1️⃣9️⃣ Buscar clave
# Pregunta al usuario qué equipo quiere consultar.
# Si existe en el diccionario → muestra sus datos.
# Si no → muestra "Equipo no encontrado".


a_buscar = input("Ingrese el nombre del equipo que quiere consultar: ")

for equipo in liga.values():
    if equipo["nombre"].lower() == a_buscar.lower():
        print(equipo)
        break
    else:
        print("Equipo no encontrado")

# 2️⃣0️⃣ Contador de resultados
# Crea una lista con resultados:
# ["local", "empate", "local", "visitante", "local"]

# Cuenta cuántas veces aparece cada resultado usando un diccionario.
resultados = ["local", "empate", "local", "visitante", "local"]

contador = {}

for i in resultados:
    if i in contador:
        contador[i] += 1
    else:
        contador[i] = 1
print(contador)