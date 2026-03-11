# 🐍 Día 7 – Manejo de Archivos en Python

## 🎯 Objetivo

Aprender a:
- Leer archivos
- Escribir archivos
- Guardar datos
- Trabajar con CSV
- Simular almacenamiento de datos deportivos

---

# 🟢 PARTE 1 – ARCHIVOS DE TEXTO (4 ejercicios)

## 1️⃣ Crear archivo

Crea un programa que cree un archivo llamado:

datos.txt

Y escriba dentro:

"Proyecto de análisis de apuestas deportivas"

---

## 2️⃣ Leer archivo

Lee el archivo `datos.txt` e imprime su contenido en pantalla.

---

## 3️⃣ Agregar contenido

Abre el archivo en modo **append** y agrega:

"Este repositorio es para practicar Python y análisis deportivo"

---

## 4️⃣ Guardar apuestas

Pide al usuario:

- monto
- cuota

Guarda esa información en un archivo llamado:

apuestas.txt

Ejemplo dentro del archivo:

100,2.30
50,1.80

---

# 🔵 PARTE 2 – ARCHIVOS CSV (4 ejercicios)

## 5️⃣ Crear CSV manual

Crea un archivo llamado:

partidos.csv

Y guarda:

equipo_local,equipo_visitante,goles_local,goles_visitante

Barcelona,Real Madrid,2,1  
PSG,Lyon,3,3  

---

## 6️⃣ Leer CSV

Lee el archivo `partidos.csv` y muestra cada línea.

---

## 7️⃣ Procesar datos

Al leer los partidos:

Determina si:

- ganó el local
- ganó el visitante
- empate

---

## 8️⃣ Guardar historial de apuestas

Crea un programa que guarde apuestas en:

historial_apuestas.csv

Formato:

monto,cuota,resultado

---

# 🟣 PARTE 3 – NIVEL PROYECTO (2 ejercicios)

## 9️⃣ Analizador de historial

Lee `historial_apuestas.csv`.

Calcula:

- total apostado
- total ganado
- ROI

---

## 🔟 Generador de partidos

Crea una lista de partidos y guárdala automáticamente en CSV.