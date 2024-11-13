# Criando um vetor vazio para armazenar as idades
idades = []

# Lendo as idades das 8 pessoas
for i in range(8):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    idades.append(idade)

# a) Calculando a média de idade
media_idade = sum(idades) / len(idades)

# b) Encontrando as posições das pessoas com mais de 25 anos
posicoes_mais_25 = [i for i, idade in enumerate(idades) if idade > 25]

# c) Encontrando a maior idade
maior_idade = max(idades)

# d) Encontrando as posições onde a maior idade foi digitada
posicoes_maior_idade = [i for i, idade in enumerate(idades) if idade == maior_idade]

# Exibindo os resultados
print(f"\nA média de idade das pessoas cadastradas é: {media_idade:.2f}")
print(f"As pessoas com mais de 25 anos estão nas posições: {posicoes_mais_25}")
print(f"A maior idade digitada foi: {maior_idade}")
print(f"As posições em que a maior idade foi digitada são: {posicoes_maior_idade}")