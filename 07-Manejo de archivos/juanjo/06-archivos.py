## 6️⃣ Leer CSV

# Lee el archivo `partidos.csv` y muestra cada línea.

import csv
with open(r"07-Manejo de archivos\partidos.csv", "r", newline="", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)