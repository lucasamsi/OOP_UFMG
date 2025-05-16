from jogador import Jogador
class Mago(Jogador):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def atacar(self):
        print("lancando bolas de fogo")

    def sofrerDanos(self):
        print("danando...")
        self.vida = (self.vida - 30)
        return self.vida

    def curar(self):
        print("curando...")
        self.vida = (self.vida + 40)
        return self.vida
    
    def ultimate(self):
        print("teletransporte para cruzada mais proxima")