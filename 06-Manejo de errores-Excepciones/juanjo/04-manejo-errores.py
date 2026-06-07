## 4️⃣ Uso de else

# Haz un programa que:

# - Intente convertir un input a float
# - Si no hay error → en else imprime "Conversión exitosa"


try:
    conversion = float(input("Ingrese una entrada: "))
except ValueError:
    print("Error de entrada ingrese un numero decimal")
else:
    print("Conversión exitosa")

