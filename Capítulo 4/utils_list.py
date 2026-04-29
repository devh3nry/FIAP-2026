# Valores fora de ordem:
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5, 3.5]

# Exibir a lista:
print(f"A lista foi criada assim: {valores}")

# Contagem de elementos 1:
contagem = valores.count(1)
print(f"A contagem de números 1 foi de: {contagem}")

# Invertendo a lista:
valores.reverse()
print(f"A lista invertida ficou assim: {valores}")

# Ordenando a lista:

valores.sort()
print(f"A lista em ordem crescente ficou assim: {valores}")

valores.sort(reverse=True)
print(f"A lista em ordem decrescente ficou assim: {valores}")

# Tamanho da lista:
quantidade = len(valores)
print(f"A quantidade de elementos na lista é: {quantidade}")

# Soma dos elementos:
soma = sum(valores)
print(f"A soma dos valores dos elementos na lista é: {soma}")