'''
## 1️⃣8️⃣ Diccionario anidado
Crea un diccionario con varios equipos:

{
  "equipo1": {"puntos": 45, "goles": 30},
  "equipo2": {"puntos": 50, "goles": 40}
}

Imprime los puntos de cada equipo.
'''
import os
os.system("cls")

equipos_fuchibol = {
    "Manchester United": 
        {
            "puntos": 48, 
            "goles": 47
        },
    "Real Madrid": 
        {
            "puntos": 60, 
            "goles": 54
        }
}

print(f"Goles del Manchester United: {equipos_fuchibol["Manchester United"]["puntos"]}")
print(f"Goles del Real Madrid: {equipos_fuchibol["Real Madrid"]["puntos"]}")

'''
## 1️⃣9️⃣ Buscar clave
Pregunta al usuario qué equipo quiere consultar.
Si existe en el diccionario → muestra sus datos.
Si no → muestra "Equipo no encontrado".
'''
search_team = input("Escribe tu equipo de futbol favorito: ")

if search_team in equipos_fuchibol:
    print("Equipo encontrado", equipos_fuchibol[search_team])
else:
    print("Equipo no encontrado")