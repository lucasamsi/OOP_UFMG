from poligonos import Poligonos
import math
class Triangulo(Poligonos):
    def __init__(self):
        super().__init__(3)

    def area(self):
        s = (self.lados[0]+self.lados[1]+self.lados[2])/2
        A = (math.sqrt(s*(s-self.lados[0])*(s-self.lados[1])*(s-self.lados[2])))
        return A

    def triRetangulo(self):

        a = self.lados[0]*self.lados[0]
        b = self.lados[1]*self.lados[1]
        c = self.lados[2]*self.lados[2]
        if((a + b == c) or (a + c == b) or (b + c == a)):
            return True
        else:
            return False