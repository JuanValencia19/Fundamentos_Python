## 6️⃣ Validación de cuota válida

# Crea una función que:

# - Pida una cuota
# - Si es menor o igual a 1 → lanza un error
# - Maneja el error mostrando mensaje personalizado

def validar_cuota():
    try:
        cuota = float(input("Ingresa una couta: "))
        if cuota <= 1:
            # lanzar error
            raise ValueError("La cuota debe ser mayor que 1")
    except ValueError as error:
        print(error)

validar_cuota()