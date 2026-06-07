## 5️⃣ Uso de finally

# Simula que estás abriendo un archivo (aunque no exista).

# Usa:
# try
# except
# finally

# En finally imprime:
# "Proceso terminado"

try:
    archivo = open("datos.txt", "r")
    print("Archivo abierto")

except FileNotFoundError:
    print("No se pudo abrir el archivo")

finally:
    print("Proceso terminado")