'''
## 3️⃣ Agregar elemento
Agrega un nuevo equipo a la lista usando `append()`.
Imprime la lista actualizada.
'''
import os
os.system("cls")

equipos_futbol = ["Manchester United", "Real Madrid", "Liverpool", "Arsenal", "Deportivo Pereira"]

equipos_futbol.append("AC Milan")
print(equipos_futbol)

'''
## 4️⃣ Eliminar elemento
Elimina un equipo específico de la lista.
Imprime la lista final.
'''

equipos_futbol.remove("Arsenal")
print(equipos_futbol)

'''
## 5️⃣ Longitud de lista
Muestra cuántos equipos hay en la lista usando `len()`.
'''

print(len(equipos_futbol))

'''
## 6️⃣ Recorrer lista con for
Recorre la lista e imprime cada equipo en una línea diferente.
'''

for i in equipos_futbol:
    print(i)