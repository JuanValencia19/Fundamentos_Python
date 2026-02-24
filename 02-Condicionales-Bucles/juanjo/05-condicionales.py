# 5️⃣ Clasificación de nota
# Pide una nota del 0 al 100 y clasifica:
# - 90–100 → Excelente
# - 70–89 → Bueno
# - 50–69 → Regular
# - Menos de 50 → Reprobado

nota = int(input("Ingresa un numero del 1 al 100 para la nota: "))

if nota >= 90 and nota <= 100:
    print("La nota esta entre 90-100 es: Excelente")
elif nota >=70 and nota <= 89:
    print("La nota esta entre 70-89 es: Bueno")
elif nota >=50 and nota <= 69:
    print("La nota esta entre 50-69 es: Regular")
else:
    print("La nota es menor que 50 es: Reprobado")
    