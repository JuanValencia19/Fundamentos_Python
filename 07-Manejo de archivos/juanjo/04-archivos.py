## 4️⃣ Guardar apuestas

# Pide al usuario:

# - monto
# - cuota

# Guarda esa información en un archivo llamado:

# apuestas.txt

# Ejemplo dentro del archivo:

# 100,2.30
# 50,1.80

monto = input("Ingresa el monto: ")
cuota = input("Ingresa la cuota: ")

with open(r"07-Manejo de archivos\apuestas.txt", "w", encoding="utf-8") as archivo:
    archivo.write(f"{monto},{cuota}\n")