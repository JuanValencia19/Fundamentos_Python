# Pide números al usuario continuamente.
# Si el usuario escribe 0:
#     termina el programa usando break.
while True:
    n = int(input("Ingrese un numero entero o ingrese 0 para finalizar el programa: "))
    if n == 0:
        print("Programa finalizado")
        break