## 2️⃣ Leer archivo

# Lee el archivo `datos.txt` e imprime su contenido en pantalla.

with open("07-Manejo de archivos\datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)

#El with es una excelente practica para hacer manejo de archivos ya que se puede ejecutar acciones y se
#  encarga automaticamente de abrir y cerrar el archivo
