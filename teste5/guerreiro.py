from jogador import Jogador
class Guerreiro(Jogador):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def atacar(self):
        print("atacando com espada")

    def sofrerDanos(self):
        print("danando...")
        self.vida = (self.vida - 15)
        return self.vida

    def curar(self):
        print("curando...")
        self.vida = (self.vida + 10)
        return self.vida
    
    def ultimate(self):
        print("espada matadora de hereges")