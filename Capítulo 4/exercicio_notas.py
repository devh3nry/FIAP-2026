notas = []

while input("Deseja inserir uma nota? S - Sim, N - Não ").upper() != "N":
    notas.append(float(input ("Digite a nota: ")))

media_aritmetica = sum(notas) / len(notas)

print(f"Para as notas digitadas, a média foi de: {media_aritmetica}")