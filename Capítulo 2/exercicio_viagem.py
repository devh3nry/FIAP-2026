valor_bruto = float(input("Digite o valor bruto da viagem: "))
categoria_assento = input("Escolha a categoria do assento: (Econômica; Executiva; Primeira Classe) ")
quantidade_viajantes = int(input("Digite a quantidade de viajantes: "))

desconto = 0

if categoria_assento == "Econômica":
    if quantidade_viajantes == 2:
        desconto = valor_bruto * 0.03
    elif quantidade_viajantes == 3:
        desconto = valor_bruto * 0.04
    elif quantidade_viajantes >= 4:
        desconto = valor_bruto * 0.05

elif categoria_assento == "Executiva":
    if quantidade_viajantes == 2:
        desconto = valor_bruto * 0.05
    elif quantidade_viajantes == 3:
        desconto = valor_bruto * 0.07
    elif quantidade_viajantes >= 4:
        desconto = valor_bruto * 0.08

elif categoria_assento == "Primeira Classe":
    if quantidade_viajantes == 2:
        desconto = valor_bruto * 0.10
    elif quantidade_viajantes == 3:
        desconto = valor_bruto * 0.15
    elif quantidade_viajantes >= 4:
        desconto = valor_bruto * 0.2

else:
    print("Categoria inválida!")
    exit()

valor_final = valor_bruto - desconto
valor_medio = valor_final / quantidade_viajantes

print(f"Valor bruto: R${valor_bruto}")
print(f"Valor de desconto: R${desconto}")
print(f"Valor líquido da viagem: R${valor_final}")
print(f"Valor médio por viajante: R$ {valor_medio}")