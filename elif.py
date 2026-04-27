pontuacao = int(input("Digite a sua pontuação: "))

if pontuacao >= 1000:
    print("Você recebeu 3gb de bônus!")
elif pontuacao >= 500:
    print("Você recebeu 1,5gb de bônus!")
elif pontuacao >= 200:
    print("Você recebeu 500mb de bônus!")
else:
    print("Você não recebeu nenhum bônus.")