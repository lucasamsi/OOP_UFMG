import math
from forma import formaGeometrica
class Triangulo(formaGeometrica):
    def __init__(self):
        self.lados = self.lerLado(3)
        self.mostraLado(3)
        self.calcular_area()
        self.calcular_perimetro()
        self.verificar_triangulo_retangulo()

    def calcular_area(self):
        s = (self.lados[0] + self.lados[1] + self.lados[2])/2
        area = (math.sqrt(s*(s-self.lados[0])*(s-self.lados[1])*(s-self.lados[2])))
        print(f"area do triangulo: {area}")
    
    def calcular_perimetro(self):
        perimetro = self.lados[0] + self.lados[1] + self.lados[2]
        print(f"perimetro do triangulo: {perimetro}")  

    def verificar_triangulo_retangulo(self):
        a = self.lados[0] * self.lados[0]
        b = self.lados[1] * self.lados[1]
        c = self.lados[2] * self.lados[2]
        if((a + b == c) or (a + c == b) or (b + c == a)):
            return print("se classifica como triangulo retangulo")

        