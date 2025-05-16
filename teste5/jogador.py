class Jogador:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        
    def vidaAtual(self):
        print(self.vida)