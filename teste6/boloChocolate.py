from bolo import Bolo
class BoloC(Bolo):
    def __init__(self, nome, dataE):
        super().__init__(nome, dataE)

    def componentes(self):
        self.recheio = input("recheio")
        self.peso = int(input("peso: (1)100 gramas - (2)500 gramas"))
        self.cobertura = input("cobertura")
        if self.peso == 1:
            self.preco = 30
        else: 
            self.preco = 50
        print(f'o recheio é {self.recheio} o pseo é o {self.peso} a cobertura é {self.cobertura}')
