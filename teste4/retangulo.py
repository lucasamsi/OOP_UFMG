from poligonos import Poligonos
class Retangulo(Poligonos):
    def __init__(self):
        super().__init__(2)
    
    def area(self):
        return (self.lados[0] * self.lados[1])
