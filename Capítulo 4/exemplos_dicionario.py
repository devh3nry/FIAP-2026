funcionarios = {}

while input("Gostaria de cadastrar um funcionário? S- Sim, N- Não: ").upper() != "N":
    nome_funcionario = input("Digite o nome do funcionário: ")
    funcao_funcionario = input("Digite sua respectiva função: ")

    funcionarios.update({nome_funcionario:funcao_funcionario})

print(funcionarios.items())