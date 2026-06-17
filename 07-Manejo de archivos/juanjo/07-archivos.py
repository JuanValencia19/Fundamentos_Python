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
        if goles_local > goles_visitante:
            print("Ganó local")
        elif goles_local < goles_visitante:
            print("Ganó visitante")
        else:
            print("Empate")



