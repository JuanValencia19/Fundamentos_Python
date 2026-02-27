# 8️⃣ Encontrar el valor mayor
# Dada una lista de cuotas, encuentra la cuota más alta sin usar `max()`.

coutas = [1.80, 2.00, 8.45, 1.14, 3.60, 4.70]

mayor = 0
for i in coutas:
    if mayor < i:
        mayor = i
print(mayor)
