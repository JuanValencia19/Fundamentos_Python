## 1️⃣ Crear archivo

# Crea un programa que cree un archivo llamado:

# datos.txt

# Y escriba dentro:

# "Proyecto de análisis de apuestas deportivas"

with open("datos.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Proyecto de análisis de apuestas deportivas")
