# 🐍 Día 3 – Listas, Tuplas y Diccionarios

## 🎯 Objetivo
Aprender a:
- Crear listas, tuplas y diccionarios
- Acceder a sus elementos
- Modificarlos
- Recorrerlos con bucles
- Usarlos en pequeños escenarios reales

---

# 🟢 PARTE 1 — LISTAS (8 ejercicios)

## 1️⃣ Crear y mostrar lista
Crea una lista con 5 equipos de fútbol.
Imprime la lista completa.

---

## 2️⃣ Acceder a elementos
Imprime:
- El primer equipo
- El último equipo

---

## 3️⃣ Agregar elemento
Agrega un nuevo equipo a la lista usando `append()`.
Imprime la lista actualizada.

---

## 4️⃣ Eliminar elemento
Elimina un equipo específico de la lista.
Imprime la lista final.

---

## 5️⃣ Longitud de lista
Muestra cuántos equipos hay en la lista usando `len()`.

---

## 6️⃣ Recorrer lista con for
Recorre la lista e imprime cada equipo en una línea diferente.

---

## 7️⃣ Sumar elementos
Crea una lista con 5 cuotas decimales.
Calcula la suma total usando un bucle.

---

## 8️⃣ Encontrar el valor mayor
Dada una lista de cuotas, encuentra la cuota más alta sin usar `max()`.

---

# 🔵 PARTE 2 — TUPLAS (4 ejercicios)

## 9️⃣ Crear tupla
Crea una tupla con información de un partido:
(nombre_local, nombre_visitante, goles_local, goles_visitante)

Imprime cada dato por separado.

---

## 🔟 Intentar modificar tupla
Intenta cambiar un valor de la tupla.
¿Qué ocurre? Explica en un comentario por qué.

---

## 1️⃣1️⃣ Desempaquetado
Desempaqueta la tupla en variables individuales:
local, visitante, goles_local, goles_visitante

---

## 1️⃣2️⃣ Comparación de goles
Usando la tupla:
Determina quién ganó el partido usando condicionales.

---

# 🟣 PARTE 3 — DICCIONARIOS (8 ejercicios)

## 1️⃣3️⃣ Crear diccionario
Crea un diccionario que represente un equipo:
{
    "nombre": "Barcelona",
    "pais": "España",
    "titulos": 27
}

Imprime cada valor usando su clave.

---

## 1️⃣4️⃣ Agregar clave
Agrega una nueva clave llamada "estadio".

---

## 1️⃣5️⃣ Modificar valor
Cambia el número de títulos.

---

## 1️⃣6️⃣ Recorrer diccionario
Imprime todas las claves y valores usando un bucle for.

---

## 1️⃣7️⃣ Diccionario de cuotas
Crea un diccionario:
{
    "local": 1.80,
    "empate": 3.40,
    "visitante": 4.20
}

Calcula la probabilidad implícita de cada resultado (1/cuota).

---

## 1️⃣8️⃣ Diccionario anidado
Crea un diccionario con varios equipos:

{
  "equipo1": {"puntos": 45, "goles": 30},
  "equipo2": {"puntos": 50, "goles": 40}
}

Imprime los puntos de cada equipo.

---

## 1️⃣9️⃣ Buscar clave
Pregunta al usuario qué equipo quiere consultar.
Si existe en el diccionario → muestra sus datos.
Si no → muestra "Equipo no encontrado".

---

## 2️⃣0️⃣ Contador de resultados
Crea una lista con resultados:
["local", "empate", "local", "visitante", "local"]

Cuenta cuántas veces aparece cada resultado usando un diccionario.