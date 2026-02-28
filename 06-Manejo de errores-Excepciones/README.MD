# 🐍 Día 6 – Manejo de Errores y Excepciones

## 🎯 Objetivo

Aprender a:
- Usar try / except
- Capturar errores específicos
- Usar else y finally
- Lanzar errores personalizados
- Validar entradas del usuario
- Hacer programas robustos

---

# 🟢 PARTE 1 — FUNDAMENTOS (5 ejercicios)

## 1️⃣ Error de división

Pide dos números al usuario.
Haz una división.

Si el usuario intenta dividir por 0:
    muestra "No se puede dividir por cero"

---

## 2️⃣ Validar número entero

Pide al usuario un número.
Si escribe algo que no sea número:
    muestra "Entrada inválida"

---

## 3️⃣ Múltiples excepciones

Pide al usuario:
- Monto
- Cuota

Captura:
- ValueError
- ZeroDivisionError

Muestra un mensaje diferente para cada error.

---

## 4️⃣ Uso de else

Haz un programa que:

- Intente convertir un input a float
- Si no hay error → en else imprime "Conversión exitosa"

---

## 5️⃣ Uso de finally

Simula que estás abriendo un archivo (aunque no exista).

Usa:
try
except
finally

En finally imprime:
"Proceso terminado"

---

# 🔵 PARTE 2 — VALIDACIONES REALES (5 ejercicios)

## 6️⃣ Validación de cuota válida

Crea una función que:

- Pida una cuota
- Si es menor o igual a 1 → lanza un error
- Maneja el error mostrando mensaje personalizado

---

## 7️⃣ Bucle con control de errores

Haz un programa que:

Mientras el usuario no ingrese un número válido:
    siga preguntando

Usa try/except dentro de un while.

---

## 8️⃣ Lanzar excepción manual

Crea una función `apostar(monto)`.

Si el monto es mayor al saldo:
    usa raise ValueError("Saldo insuficiente")

---

## 9️⃣ Sistema de apuesta robusto

Crea un sistema que:

- Pida monto
- Pida cuota
- Calcule ganancia

Debe manejar:
- Letras
- División por cero
- Cuotas inválidas

El programa NO debe romperse nunca.

---

## 🔟 Validación con múltiples condiciones

Pide edad.

Si:
- Edad < 0 → error
- Edad < 18 → mensaje "No permitido"
- Edad válida → mensaje correcto

Usa raise para edad negativa.

---

# 🟣 PARTE 3 — NIVEL PROYECTO (4 ejercicios)

## 1️⃣1️⃣ Función segura de promedio

Crea una función que calcule promedio de lista.

Si la lista está vacía:
    lanza una excepción personalizada.

---

## 1️⃣2️⃣ Clase con manejo de errores

Modifica tu clase CuentaBancaria:

En retirar():
    si saldo insuficiente → raise Exception

Maneja el error al usar el método.

---

## 1️⃣3️⃣ Simulador seguro

Crea una clase SimuladorApuestas que:

- Maneje errores si el usuario mete texto
- No permita apostar más del saldo
- Siempre continúe ejecutándose

---

## 1️⃣4️⃣ Crear tu propia excepción

Crea una excepción personalizada:

class CuotaInvalidaError(Exception):
    pass

Úsala cuando cuota <= 1.