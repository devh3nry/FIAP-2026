voto1 = (input("Escolha em qual console você deseja votar: PLAYSTATION; XBOX; NINTENDO) "))
voto2 = (input("Escolha em qual console você deseja votar: PLAYSTATION; XBOX; NINTENDO) "))
voto3 = (input("Escolha em qual console você deseja votar: PLAYSTATION; XBOX; NINTENDO) "))
voto4 = (input("Escolha em qual console você deseja votar: PLAYSTATION; XBOX; NINTENDO) "))
voto5 = (input("Escolha em qual console você deseja votar: PLAYSTATION; XBOX; NINTENDO) "))

playstation = 0
xbox = 0
nintendo = 0

if voto1 == "PLAYSTATION":
    playstation = playstation + 1
elif voto1 == "XBOX":
    xbox = xbox + 1
elif voto1 == "NINTENDO":
    nintendo = nintendo + 1

if voto2 == "PLAYSTATION":
    playstation = playstation + 1
elif voto2 == "XBOX":
    xbox = xbox + 1
elif voto2 == "NINTENDO":
    nintendo = nintendo + 1

if voto3 == "PLAYSTATION":
    playstation = playstation + 1
elif voto3 == "XBOX":
    xbox = xbox + 1
elif voto3 == "NINTENDO":
    nintendo = nintendo + 1

if voto4 == "PLAYSTATION":
    playstation = playstation + 1
elif voto4 == "XBOX":
    xbox = xbox + 1
elif voto4 == "NINTENDO":
    nintendo = nintendo + 1

if voto5 == "PLAYSTATION":
    playstation = playstation + 1
elif voto5 == "XBOX":
    xbox = xbox + 1
elif voto5 == "NINTENDO":
    nintendo = nintendo + 1

else:
    print("Console inexistente. Voto anulado.")

print(f"PLAYSTATION: {playstation}")
print(f"XBOX: {xbox}")
print(f"NINTENDO: {nintendo}")

if playstation > xbox and playstation > nintendo:
    print("O console escolhido foi o PLAYSTATION!")
elif xbox > playstation and xbox > nintendo:
    print("O console escolhido foi o XBOX!")
elif nintendo > playstation and nintendo > xbox:
    print("O console escolhido foi o NINTENDO!")
else:
    print("Houve empate na votação.")