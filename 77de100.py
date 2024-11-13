# Criando uma lista vazia para armazenar os nomes
nomes = []

# Lendo 7 nomes e armazenando na lista
for i in range(7):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

# Mostrando os nomes na ordem inversa
print("\nNomes na ordem inversa:")
for nome in reversed(nomes):
    print(nome)