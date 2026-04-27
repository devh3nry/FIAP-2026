idade = int(input ("Digite a sua idade: "))
bpm = float(input ("Digite o número de BPM: "))

if idade <= 2:
    minimo = 120
    maximo = 140
elif idade >= 3 and idade <= 7:
    minimo = 120
    maximo = 140
elif idade >= 8 and idade <= 17:
    minimo = 80
    maximo = 100
elif idade >= 18 and idade <= 59:
    minimo = 70
    maximo = 80
else:
    minimo = 50
    maximo = 60

if bpm < minimo:
    print("BPM abaixo do normal!")
elif bpm > maximo:
    print ("BPM acima do normal!")
else:
    print("BPM normal.")