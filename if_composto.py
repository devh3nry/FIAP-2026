rm = input("Digite o número da sua matrícula: ")
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Cadastro confirmado, aluno de RM {}!".format(rm))
    print(f"Cadastro confirmado, aluno de RM {rm}!")
else:
    autorizacao = input("Você possui autorização dos seus responsáveis? S- SIM | N- NÃO: ")
    if autorizacao == "S" or autorizacao == "s":
        print(f"Cadastrado confirmado, aluno de RM {rm}!")
    else:
        print(f"Cadastro não realizado, aluno menor de idade e sem autorização dos responsáveis. Sua idade: {idade}")

