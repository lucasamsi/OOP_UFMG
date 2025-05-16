from Funcionario import funcionario
class horista(funcionario):
    def __init__(self, nome, hora, pagamentoH):
        super().__init__(nome)
        self.hora = hora
        self.pagamentoH = pagamentoH

    def calculoPagamento(self):
        salario = (self.hora * self.pagamentoH)
        return salario
    