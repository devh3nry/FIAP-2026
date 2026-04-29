username = input("Digite o seu usuário: ")
password = input("Digite a sua senha: ")

if username.lower() == "darth_vader" and password == "1138":
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorreto.")