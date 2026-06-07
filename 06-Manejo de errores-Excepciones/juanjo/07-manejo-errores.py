## 7️⃣ Bucle con control de errores

# Haz un programa que:

# Mientras el usuario no ingrese un número válido:
#     siga preguntando

# Usa try/except dentro de un while.


while True:
    try:
        valido = int(input("Ingrese un numero: "))
        break
    except ValueError:
        print("Estas ingresando una entrada invalida")
