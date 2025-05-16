from mago import Mago
from guerreiro import Guerreiro

""" def criaJogador():
    while True:
        nome = input("Nome: ")
        tipo = input("(1) para Mago - (2) para Guerreiro")
        if tipo == 1:
            vida = 200
            jogador = Mago(nome, vida)
            return jogador, 'mago'
        elif tipo == 2:
            vida = 300
            jogador = Guerreiro(nome, vida)
            return jogador
        else: print("numero invalido") """

jogador1 = Mago('Luiz Inacio', 200)
jogador2 = Guerreiro('Ricardo Coração de leão', 300)

jogador1.atacar()
jogador1.sofrerDanos()
jogador1.vidaAtual()
jogador1.curar()
jogador1.vidaAtual()
jogador1.ultimate()

jogador2.atacar()
jogador2.sofrerDanos()
jogador2.vidaAtual()
jogador2.curar()
jogador2.vidaAtual()
jogador2.ultimate()

