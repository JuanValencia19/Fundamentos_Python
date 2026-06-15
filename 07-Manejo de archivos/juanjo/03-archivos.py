## 3️⃣ Agregar contenido

# Abre el archivo en modo **append** y agrega:

# "Este repositorio es para practicar Python y análisis deportivo"

with open("07-Manejo de archivos\datos.txt", "a", encoding="utf-8") as archivo:
    archivo.write("\nEste repositorio es para practicar Python y análisis deportivo")