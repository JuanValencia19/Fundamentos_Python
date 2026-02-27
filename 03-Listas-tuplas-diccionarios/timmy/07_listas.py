'''
## 7️⃣ Sumar elementos
Crea una lista con 5 cuotas decimales.
Calcula la suma total usando un bucle.
'''
import os
os.system("cls")

list_cuotas = [2.4, 3.5, 1.2, 2.1, 2]
suma = 0

for i in list_cuotas:
    suma += i
    print(round(suma, 2))
    
'''
## 8️⃣ Encontrar el valor mayor
Dada una lista de cuotas, encuentra la cuota más alta sin usar `max()`.
'''

list_cuotas.sort()
print(list_cuotas)
print(f"Valor mayor de la lista: {list_cuotas[-1]}")