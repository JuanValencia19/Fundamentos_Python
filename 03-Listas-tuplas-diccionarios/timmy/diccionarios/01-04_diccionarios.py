'''
## 1️⃣3️⃣ Crear diccionario
Crea un diccionario que represente un equipo:
{
    "nombre": "Barcelona",
    "pais": "España",
    "titulos": 27
}

Imprime cada valor usando su clave.
'''
import os
os.system("cls")

equipo = {
    "nombre": "Manchester United",
    "pais": "Inglaterra",
    "titulos": 68
}
    
for clave, valor in equipo.items():
    print(valor)

'''
## 1️⃣4️⃣ Agregar clave
Agrega una nueva clave llamada "estadio".
'''

equipo["estadio"] = "Old Trafford"
print(equipo)

'''
## 1️⃣5️⃣ Modificar valor
Cambia el número de títulos.
'''

equipo["titulos"] = 70
print(equipo)

'''
## 1️⃣6️⃣ Recorrer diccionario
Imprime todas las claves y valores usando un bucle for.
'''

for clave, valor in equipo.items():
    print(f"{clave} : {valor}")