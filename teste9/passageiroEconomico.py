from passageiroAviao import PassageiroAviao
class PassageiroEconomico(PassageiroAviao):
    def __init__(self):
        self.nome = self.defineNome()
        self.poltrona = self.definePoltrona()
    
    def defineNome(self):
        while True:
            nome = input("Digite o nome do passageiro: ")
            verificar = nome.isalpha()
            if verificar:
                self.nome = nome
                return self.nome
            else: print("nome invalido, use somente letras")

    def definePoltrona(self):
        while True:
            poltrona = int(input("numero da poltrona(1 - 40): "))
            if poltrona <= 40 and poltrona >= 1:
                self.poltrona = poltrona
                return self.poltrona
            else: print("numero deve ser entre 1 e 40")

    def fazer_check_in(self):
        if self.poltrona and self.nome:
            print(f"{self.nome} fez o check in na poltrona {self.poltrona}")
        else: print("termine o cadastro")


    def passar_pela_seguranca(self):
        if self.poltrona and self.nome:
            while True: 
                numero = int(input("para liberar a entrada, digite o numero da poltrona escolhida:"))
                if numero == self.poltrona:
                    print(f"{self.nome} passou pela seguranca")
                    break
                else: print("a poltrona inserida nao eh a mesma escolhida, tente novamente")

    def embarcar(self):
        if self.nome and self.poltrona:
            print(f"{self.nome} embarcou")
        else: print("embarcando")
        

