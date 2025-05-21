from abc import ABC, abstractmethod
class formaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    def lerLado(self, tamanho):
        # n = int(input("numero de lados"))
        lados = []

        for i in range(tamanho):
            lado = float(input("tamanho do lado: "))
            lados.append(lado)     
        return lados

    def mostraLado(self, tipo):
        print("os lados da forma sao: ")
        if tipo == 3:
            for i in range(3):
                print(self.lados[i])
        elif tipo == 2:
            for i in range(2):
                print(self.lados[0])
                print(self.lados[1])
        else: 
            for i in range(4):
                print(self.lados[0])

