## 7️⃣ Procesar datos

# Al leer los partidos:

# Determina si:

# - ganó el local
# - ganó el visitante
# - empate

import csv


with open(r"07-Manejo de archivos\partidos.csv", "r", newline="", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    next(lector)      
    for fila in lector:
        goles_local = int(fila[2])
        goles_visitante = int(fila[3])
        equipo_local = (fila[0])
        equipo_visitante = (fila[1])
        if goles_local > goles_visitante:
            print(f"Ganó local: {equipo_local} {goles_local} vs {equipo_visitante} {goles_visitante}")
        elif goles_local < goles_visitante:
            print(f"Ganó visitante: {equipo_local} {goles_local} vs {equipo_visitante} {goles_visitante}")
        else:
            print(f"Empate: {equipo_local} {goles_local} vs {equipo_visitante} {goles_visitante}")



