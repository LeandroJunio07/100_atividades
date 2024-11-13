# Inicializando os vetores para armazenar os nomes e idades
nomes = []
idades = []

# Lendo os dados de 9 pessoas
for i in range(9):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    
    nomes.append(nome)  # Armazenando o nome no vetor nomes
    idades.append(idade)  # Armazenando a idade no vetor idades

# Exibindo os dados das pessoas menores de idade
print("\nPessoas menores de idade:")
for i in range(9):
    if idades[i] < 18:  # Verificando se a pessoa é menor de idade
        print(f"Nome: {nomes[i]}, Idade: {idades[i]}")