from forma import formaGeometrica
class Retangulo(formaGeometrica):
    def __init__(self):
        self.lados = self.lerLado(2) # retangulo recebe 2 lados iguais
        self.mostraLado(2)
        self.calcular_area()
        self.calcular_perimetro()

    def calcular_area(self):
        area = (self.lados[0] * self.lados[1])
        print(f"area do retangulo: {area}")
    
    def calcular_perimetro(self):
        perimetro = (self.lados[0] * 2) + (self.lados[1] * 2)
        print(f"perimetro do retangulo: {perimetro}")