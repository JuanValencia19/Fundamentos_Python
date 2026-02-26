'''
Define una contraseña guardada en una variable.
Pide al usuario que la ingrese.

Si coincide → "Acceso concedido"
Si no → "Acceso denegado"
'''
import os
os.system("cls")

password = "admin123"

valid_password = input("Ingresa la contraseña para ingresar al sistema: ")

while valid_password != password:
    print("Contraseña incorrecta.")
    valid_password = input("Ingresa nuevamente la contraseña para ingresar al sistema: ")
    
if valid_password == password:
    print("Acceso concedido")
else:
    print("Acceso denegado")