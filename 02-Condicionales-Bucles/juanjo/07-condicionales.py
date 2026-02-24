# 7️⃣ Validación de contraseña
# Define una contraseña guardada en una variable.
# Pide al usuario que la ingrese.

# Si coincide → "Acceso concedido"
# Si no → "Acceso denegado"

contrasena = "hola contrasena python"
usuario_input = input("Ingresa la contrasena del programa: ")

if contrasena == usuario_input:
    print("Acceso concedido")
else:
    print("Acceso denegado")