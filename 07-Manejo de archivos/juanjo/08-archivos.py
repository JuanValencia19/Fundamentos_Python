## 8️⃣ Guardar historial de apuestas

# Crea un programa que guarde apuestas en:

# historial_apuestas.csv

# Formato:

# monto,cuota,resultado

import csv

with open(r"07-Manejo de archivos\historial_apuesta.csv", "a", encoding="utf-8", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["monto", "cuota", "resultado"])
    while True:
        print("Bienvenido al historial de apuestas. Ingresa 0 si deseas salir")
        monto = int(input("Ingresa el monto: "))
        cuota = float(input("Ingresa la couta en numero flotante: "))
        resultado = input("Ingresa si ganaste o perdiste la apuesta: ")
        if monto == 0:
            break
        else:
            escritor.writerow([monto, cuota, resultado])
            print("Apuesta guardada correctamente")