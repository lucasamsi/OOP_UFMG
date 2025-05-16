from Funcionario import funcionario
class assalariado(funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario

    def calculoPagamento(self):
        return self.salario