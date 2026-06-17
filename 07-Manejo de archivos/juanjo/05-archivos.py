## 5️⃣ Crear CSV manual

# Crea un archivo llamado:

# partidos.csv

# Y guarda:

# equipo_local,equipo_visitante,goles_local,goles_visitante

# Barcelona,Real Madrid,2,1  
# PSG,Lyon,3,3 

import csv

with open(r"07-Manejo de archivos\partidos.csv", "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["equipo_local", "equipo_visitante", "goles_local", "goles_visitante"])
    escritor.writerow(["Barcelona", "Real Madrid", 2, 1])
    escritor.writerow(["PSG", "Lyon", 3, 3])