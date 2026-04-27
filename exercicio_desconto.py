cupom = input("Digite o cupom de desconto: ")
valor_compra = float(input ("Digite o valor da sua compra: "))

if cupom.upper() == "NIVER10":
    valor_compra = valor_compra * 0.9
    print("Você aplicou um cupom de desconto!")
else:
    print("Você digitou um cupom de desconto inválido.")

print(f"Valor final da compra é de R${valor_compra}")