## 1️⃣4️⃣ Crear tu propia excepción

# Crea una excepción personalizada:

# class CuotaInvalidaError(Exception):
#     pass

# Úsala cuando cuota <= 1.

class CuotaInvalidaError(Exception):
    pass


def validar_cuota(cuota):
    if cuota <= 1:
        raise CuotaInvalidaError("La cuota debe ser mayor que 1")
    print("Cuota válida")

try:
    validar_cuota(1.5)
    validar_cuota(0.9)
except CuotaInvalidaError as error:
    print(error)