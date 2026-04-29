def velocidade_media():
    distancia = float(input ("Digite a distância percorrida (Em KM): "))
    tempo = float(input ("Digite o tempo gasto na viagem (Em Horas): "))
    velocidade_media = distancia / tempo
    print(f"A velocidade média foi de {velocidade_media} KM/h")

velocidade_media()