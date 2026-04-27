valor_compra = float(input ("Digite o valor da sua compra: "))
cupom = input("Digite um cupom de desconto: ")


if valor_compra >= 1000.0 or cupom.upper() == "FESTA":
    valor_compra = valor_compra * 0.9
    print("Você recebeu um cupom de desconto de 10%!")
else:
    print("Você não possui o direito ao desconto de 10%.")

print(f"A sua compra teve o valor de R${valor_compra}")