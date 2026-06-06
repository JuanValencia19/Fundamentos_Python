"""
Se debe crear lo siguiente una clase estudiante
que tenga los siguientes atributos(nombre, edad y grado). Con los metodos de: estudiar() que imprima "el estudiante(nombre) esta estudiando"
Crear un objeto estudiante y usar metodo estudiar. Se debe interactuar con el usuario y este debe brindar los atributos.
"""

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print(f"el estudiante {self.nombre} esta estudiando")

estudiante1 = Estudiante("","","")

nombre_estudiante = str(input("Ingrese el nombre del estudiante: "))

edad_estudiante = int(input("Ingrese la edad del estudiante: "))

grado_estudiante = input("Ingrese el grado del estudiante")

estudiante1.nombre = nombre_estudiante

estudiante1.edad = edad_estudiante

estudiante1.grado = grado_estudiante

estudiante1.estudiar()