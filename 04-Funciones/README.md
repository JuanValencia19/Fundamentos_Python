# 🐍 Día 4 – Funciones en Python

## 🎯 Objetivo
Aprender a:
- Crear funciones con `def`
- Usar parámetros
- Retornar valores con `return`
- Dividir problemas en pequeñas funciones
- Escribir código modular

---

# 🟢 PARTE 1 — FUNDAMENTOS (5 ejercicios)

## 1️⃣ Función de saludo
Crea una función llamada `saludar()` que imprima:
"Bienvenido al sistema de análisis deportivo"

Llama la función.

---

## 2️⃣ Función con parámetro
Crea una función `saludar_usuario(nombre)` que imprima:
"Hola, [nombre]"

Llama la función pasando tu nombre.

---

## 3️⃣ Función suma
Crea una función `sumar(a, b)` que retorne la suma.
Imprime el resultado al llamarla.

---

## 4️⃣ Función para calcular cuota
Crea una función `probabilidad(cuota)` que retorne:

1 / cuota

Muestra el resultado.

---

## 5️⃣ Función par o impar
Crea una función `es_par(numero)` que retorne:
True si es par
False si es impar

---

# 🔵 PARTE 2 — FUNCIONES CON LÓGICA (6 ejercicios)

## 6️⃣ Ganancia de apuesta
Crea una función:

calcular_ganancia(monto, cuota, gano)

Si ganó → retorna monto * cuota
Si perdió → retorna 0

---

## 7️⃣ Clasificador de cuota
Crea una función `clasificar_cuota(cuota)` que retorne:

- "Favorito" si cuota < 1.8
- "Equilibrado" si está entre 1.8 y 2.5
- "No favorito" si es mayor a 2.5

---

## 8️⃣ Promedio de lista
Crea una función `calcular_promedio(lista)` que reciba una lista de números y retorne el promedio.

NO uses sum() ni len() (hazlo manual con bucle).

---

## 9️⃣ Mayor valor
Crea una función `mayor_valor(lista)` que retorne el número mayor sin usar max().

---

## 🔟 Contador de resultados
Crea una función que reciba una lista como:

["local", "empate", "local", "visitante"]

Y retorne un diccionario con el conteo.

---

## 1️⃣1️⃣ Función que llama otra función
Crea:

- Una función `probabilidad(cuota)`
- Una función `valor_esperado(monto, cuota, prob_real)`

La función valor_esperado debe usar la función probabilidad dentro de su cálculo.

---

# 🟣 PARTE 3 — NIVEL PROYECTO (4 ejercicios)

## 1️⃣2️⃣ Analizador de partido
Crea una función que reciba:

- goles_local
- goles_visitante

Y retorne:
"Local ganó"
"Visitante ganó"
"Empate"

---

## 1️⃣3️⃣ Simulación de 5 apuestas
Crea una función que:

- Reciba una lista de cuotas
- Suponga que siempre ganas
- Retorne la ganancia total apostando 100 a cada una

---

## 1️⃣4️⃣ Función con validación
Crea una función que pida al usuario una cuota.
Si la cuota es menor o igual a 1, vuelva a pedirla.

---

## 1️⃣5️⃣ Mini sistema modular
Divide este programa en funciones:

- pedir_datos()
- calcular_probabilidad()
- mostrar_resultado()

Haz que trabajen juntas.