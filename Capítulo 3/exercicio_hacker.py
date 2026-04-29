minutos = int(input ("Digite os minutos atuais do horário atual: "))

fatorial = minutos

for i in range (1, minutos):
    fatorial = fatorial * i

print(f"A senha para desbloqueio do sistema é: LIBERDADE{fatorial}")