## 🔟 Sistema modular

# Crea una clase `AnalizadorCuotas` con:

# - método `probabilidad(cuota)`
# - método `clasificar(cuota)`

# Y que ambos trabajen juntos.

class AnalizadorCuotas:
    def __init__(self, cuota):
        self.cuota = cuota
    def probabilidad(self):
        return 1 / self.cuota
    def clasificar(self):
        prob = self.probabilidad()
        if prob >= 0.70:
            return "Cuota favorita"
        elif prob >= 0.40:
            return "Cuota media"
        else:
            return "Cuota poco probable"        
analisis = AnalizadorCuotas(1.50)
print(analisis.probabilidad())
print(analisis.clasificar())