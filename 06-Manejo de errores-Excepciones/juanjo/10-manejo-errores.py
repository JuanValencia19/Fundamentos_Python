## 🔟 Validación con múltiples condiciones

# Pide edad.

# Si:
# - Edad < 0 → error
# - Edad < 18 → mensaje "No permitido"
# - Edad válida → mensaje correcto

# Usa raise para edad negativa.

try:
    edad = int(input("Ingresa tu edad: "))
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    elif edad < 18:
        print("No permitido")
    else:
        print("Edad válida puedes ingresar")
except ValueError as error:
    print(error)


