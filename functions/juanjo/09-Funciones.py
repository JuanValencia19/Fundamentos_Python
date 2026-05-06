#  9️⃣ Mayor valor
# Crea una función `mayor_valor(lista)` que retorne el número mayor sin usar max().

def mayor_valor(lista):
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor

print(mayor_valor([15,70,64,59,85,23,10]))
