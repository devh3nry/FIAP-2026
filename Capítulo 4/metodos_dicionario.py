produtos = {
    "Cafeteira": 100.00,
    "Liquidificador": 250.00,
    "Lixeira": 50.00,
    "Air Fryer": 500,
    "Garfo": 2.50,
    "Colher": 2.00
}

print(produtos)

print("---------------------")

produtos.pop("Cafeteira")
print(produtos)

print("---------------------")

produtos.popitem()
print(produtos)

print("---------------------")

produtos.clear()
print(produtos)