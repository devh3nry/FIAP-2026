frutas = ["banana", "maçã", "pêra", "goiaba"]

print(f"A lista original contém: \n {frutas}")

# Inserção no final da lista:
frutas.append("uva")
print(f"Após a inserção, a lista contém: \n {frutas}")

# Inserção no final da lista com input:

frutas.append(input ("Insira o nome de uma fruta: "))
print(f"Após a inserção, a lista contém: \n {frutas}")

# Inserção em posição:
frutas.insert(0, "abiu")
print(f"Após a inserção na posição indicada, a lista contém: \n {frutas}")