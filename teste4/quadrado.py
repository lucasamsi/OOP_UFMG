from poligonos import Poligonos

class Quadrado(Poligonos):
    def __init__(self):
        super().__init__(1)
        self.lados = super().lerLado()

    
    def area(self):
        return (self.lados[0]*self.lados[0])
