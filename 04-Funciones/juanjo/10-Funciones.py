#  9️⃣ Mayor valor
# Crea una función `mayor_valor(lista)` que retorne el número mayor sin usar max().
def mayor_valor(lista):
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor
print(mayor_valor([1,3,6,19,10,8,0,77,9,18]))