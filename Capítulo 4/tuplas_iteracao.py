categorias = ("A", "B", "C", "D", "E")

categoria_usuario = input("Insira qual a sua categoria da CNH: ")

if categoria_usuario in categorias:
    print("Categoria existente!")
else:
    print("Categoria inexistente!")