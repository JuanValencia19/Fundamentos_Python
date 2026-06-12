## 1️⃣1️⃣ Función segura de promedio

# Crea una función que calcule promedio de lista.

# Si la lista está vacía:
#     lanza una excepción personalizada.

def calcular_promedio(lista):
    if lista == []:
        raise ValueError("No puedes dejar la lista vacia")
    promediador = 0
    contador = 0
    for i in lista:
        if type(i) == str:
            raise TypeError("Todos los elementos deben ser números")
        promediador += i
        contador += 1
    promedio = promediador / contador
    return promedio 
try:
    print(calcular_promedio([1,8,9,11,5,3]))
    # calcular_promedio([])
except ValueError as error:
    print(error)
except TypeError as error:
    print(error)