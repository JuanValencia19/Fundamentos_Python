# 🐍 Día 5 – Clases y Objetos (POO)

## 🎯 Objetivo

Aprender a:
- Crear clases
- Instanciar objetos
- Definir atributos
- Crear métodos
- Modelar entidades reales
- Pensar en términos de objetos

---

# 🟢 PARTE 1 — FUNDAMENTOS (5 ejercicios)

## 1️⃣ Crear tu primera clase

Crea una clase llamada `Jugador`.

Debe tener:
- nombre
- edad
- posicion

Crea un objeto e imprime sus atributos.

---

## 2️⃣ Método dentro de la clase

Agrega un método llamado `presentarse()` que imprima:

"Hola, soy [nombre] y juego como [posicion]"

---

## 3️⃣ Clase Equipo

Crea una clase `Equipo` con:

- nombre
- pais
- titulos

Crea dos equipos diferentes e imprime su información.

---

## 4️⃣ Modificar atributos

Crea una clase `CuentaBancaria` con:

- titular
- saldo

Crea un método `depositar(monto)` que aumente el saldo.

Prueba depositando dinero.

---

## 5️⃣ Método condicional

En `CuentaBancaria`, crea un método `retirar(monto)`:

- Si hay saldo suficiente → resta el monto
- Si no → imprime "Fondos insuficientes"

---

# 🔵 PARTE 2 — NIVEL INTERMEDIO (5 ejercicios)

## 6️⃣ Clase Partido

Crea una clase `Partido` con:

- local
- visitante
- goles_local
- goles_visitante

Agrega un método `resultado()` que retorne:
- "Ganó local"
- "Ganó visitante"
- "Empate"

---

## 7️⃣ Clase Apuesta

Crea una clase `Apuesta` con:

- monto
- cuota
- gano (True/False)

Agrega un método `calcular_ganancia()` que:

- Retorne monto * cuota si ganó
- Retorne 0 si perdió

---

## 8️⃣ Contador interno

Crea una clase `SimuladorApuestas` que tenga:

- saldo inicial
- método para apostar
- método para mostrar saldo

Cada apuesta debe modificar el saldo.

---

## 9️⃣ Lista de objetos

Crea 3 objetos `Partido` y guárdalos en una lista.

Recorre la lista y muestra el resultado de cada partido usando el método `resultado()`.

---

## 🔟 Sistema modular

Crea una clase `AnalizadorCuotas` con:

- método `probabilidad(cuota)`
- método `clasificar(cuota)`

Y que ambos trabajen juntos.

---

# 🟣 PARTE 3 — NIVEL PROYECTO (4 ejercicios)

## 1️⃣1️⃣ Clase Equipo con estadísticas

Crea una clase `Equipo` con:

- nombre
- goles_a_favor
- goles_en_contra

Agrega un método que calcule diferencia de gol.

---

## 1️⃣2️⃣ Historial de partidos

Haz que la clase `Equipo` tenga una lista interna llamada `historial`.

Crea un método `agregar_partido(partido)`.

---

## 1️⃣3️⃣ Simulación básica

Crea una clase `SimuladorTemporada` que:

- Reciba una lista de equipos
- Permita simular partidos
- Actualice estadísticas

(No necesitas hacerlo complejo, solo lógica básica)

---

## 1️⃣4️⃣ Mini sistema completo

Crea:

- Clase `Equipo`
- Clase `Partido`
- Clase `Apuesta`

Haz que trabajen juntas en un pequeño flujo:

1. Se crea un partido
2. Se hace una apuesta
3. Se muestra el resultado
4. Se calcula la ganancia