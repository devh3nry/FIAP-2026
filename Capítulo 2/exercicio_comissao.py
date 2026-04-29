print("BASIC")
print("SILVER")
print("GOLD")
print("PLATINUM")

tipo_assinatura = input("Escolha de acordo com as opções acima, qual a sua assinatura: ")

faturamento_anual = float(input ("Digite o seu faturamento anual: "))
taxa_comissao = 0

match tipo_assinatura:
    case "BASIC":
        comissao = faturamento_anual * 0.3
    case "SILVER":
        comissao = faturamento_anual * 0.2
    case "GOLD":
        comissao = faturamento_anual * 0.1
    case "PLATINUM":
        comissao = faturamento_anual * 0.05

print(f"Você possui a assinatura {tipo_assinatura}, faturou R${faturamento_anual} no ano, e terá de pagar R${comissao} de comissão.")