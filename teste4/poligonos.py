class Poligonos:
    def __init__(self,numerolados):
        self.numerolados = numerolados

    def lerLado(self):
        n = self.numerolados
        self.lados = []

        for i in range(n):
            lado = float(input("tamanho do lado: "))
            self.lados.append(lado)     
        return self.lados

    def mostraLado(self):
        for i in range(self.numerolados):
            print(self.lados[i])