qtd_transacoes = int (input ("Digite quantas transações você realizou hoje: "))

valor_total = 0
valor_medio = 0

for i in range (qtd_transacoes):
    if i < qtd_transacoes:
        valor_transacao = float (input (f"Digite o valor desta transação: "))
        valor_total = valor_total + valor_transacao
        valor_medio = valor_total / qtd_transacoes

print(f"Valor total das transações: {valor_total}")
print(f"Valor médio das transações: {valor_medio}")