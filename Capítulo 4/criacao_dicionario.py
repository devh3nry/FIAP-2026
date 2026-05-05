produtos = {
    "Cafeteira": 100.00,
    "Liquidificador": 250.00,
    "Lixeira": 50.00,
    "Garfo": 2.50
}

# print(produto["nome"])
# print(produto.get("nome"))
# (produto.keys())

# for i in produto.keys():
# print(produto[i])

# print(len(produto.values()))
# print("Cafeteira" in produto.values())

print(produtos.items())

for nome_produto, preco in produtos.items():
    print(f"O produto {nome_produto} custa {preco}")