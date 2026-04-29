numero_digitado = int(input ("Digite um número inteiro: "))

anterior1 = 1
anterior2 = 0

for numero_elementos in range (1, numero_digitado + 1, 1):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = atual
    if numero_digitado == atual:
        print("Ação bem sucedida!")
        break
    elif numero_digitado < atual:
        print("Ação mal-sucedida.")
        break

print("Sistema encerrando...")