posicao_inimigo = [(0, 1), (10, 5), (10, 10)]

while len(posicao_inimigo) > 0:

    posicao_ataque_usuario_x = int(input("Informe a posição X a ser atacada: "))
    posicao_ataque_usuario_y = int(input("Informe a posição Y a ser atacada: "))

    if (posicao_ataque_usuario_x, posicao_ataque_usuario_y) in posicao_inimigo:
        print("Você acertou um inimigo!")
        posicao_inimigo.remove((posicao_ataque_usuario_x, posicao_ataque_usuario_y))
    else:
        print("Você errou. Tente novamente!")

    print(f"Restam {len(posicao_inimigo)} inimigos.")