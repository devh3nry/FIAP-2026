qtd_alimentos = int(input ("Digite quantos alimentos você comeu hoje: "))

calorias_total = 0

for i in range (qtd_alimentos):
    if i < qtd_alimentos:
        calorias = int (input("Digite quantas calorias possui este alimento: "))
        calorias_total = calorias_total + calorias


print(f"Você consumiu: {calorias_total} calorias hoje!")