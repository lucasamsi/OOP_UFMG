from Assalariado import assalariado
from Horista import horista

def criaH():
    nome = input("nome: ")
    horas = float(input("horas trabalhadas: "))
    salario = float(input("salario por hora: "))
    return horista(nome, horas, salario)

def criaA():
    nome = input("nome: ")
    salario = float(input("salario: "))
    return assalariado(nome, salario)

def main():
    contratados = []
    
    while True:
        print("1 para ver funcionarios")
        print("0 para adicionar funcionarios")

        escolha = input(": ")
        if escolha == '0':
            escolhatipo = input("1 para Horista e 0 para Assalariado: ")
            if escolhatipo == '1':
                novo = criaH()
                contratados.append(novo)
            else:
                novo = criaA()
                contratados.append(novo)
        elif escolha == '1':
            for c in contratados:
                print(f"{c.nome} ganha R$ {c.calculoPagamento():.2f}")
        else:
            break

if __name__ == "__main__":
    main()