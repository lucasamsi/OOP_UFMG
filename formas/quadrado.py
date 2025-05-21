from forma import formaGeometrica
class Quadrado(formaGeometrica):
    def __init__(self):
        self.lados = self.lerLado(1) # quadrado com todos os lados iguais
        self.mostraLado(1)
        self.calcular_area()
        self.calcular_perimetro()   

    def calcular_area(self):
        area = (self.lados[0] * self.lados[0])
        print(f"area do quadrado: {area}")
    
    def calcular_perimetro(self):
        perimetro = self.lados[0] * 4
        print(f"perimetro do quadrado: {perimetro}")