# Inicializando os vetores para armazenar nome, sexo e salário
nomes = []
sexos = []
salarios = []

# Lendo os dados de 5 funcionários
for i in range(5):
    nome = input(f"Digite o nome do {i+1}º funcionário: ")
    sexo = input(f"Digite o sexo do {i+1}º funcionário (M/F): ").upper()
    salario = float(input(f"Digite o salário do {i+1}º funcionário: R$ "))
    
    # Armazenando os dados nos respectivos vetores
    nomes.append(nome)
    sexos.append(sexo)
    salarios.append(salario)

# Exibindo os dados das funcionárias mulheres que ganham mais de R$5.000
print("\nFuncionárias mulheres que ganham mais de R$5.000:")
for i in range(5):
    if sexos[i] == 'F' and salarios[i] > 5000:
        print(f"Nome: {nomes[i]}, Sexo: {sexos[i]}, Salário: R${salarios[i]:.2f}")