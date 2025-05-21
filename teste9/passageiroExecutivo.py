from passageiroAviao import PassageiroAviao
class PassageiroExecutivo(PassageiroAviao):
    def __init__(self):
        super.__init__()

    def defineNome(self):
        self.nome = input("nome: ")
        return self.poltrona

    def definePoltrona(self):
        self.poltrona = int(input("numero da poltrona: "))
        return self.poltrona

    def fazer_check_in(self):
        print(f"{self.nome} fez o check in na poltrona {self.poltrona} da classe executiva")

    def passar_pela_seguranca(self):
        if self.nome == "Gabi":
            print("gabi foi barrada na seguranca por mendigar")
        else: print("passou pela seguranca")

    def embarcar(self):
        if self.nome == "Gabi":
            print("gabi foi levada pra el salvador") 
        else: print("embarcando")