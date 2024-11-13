# Criando um vetor vazio para armazenar as notas dos alunos
notas = []

# Lendo as notas dos 10 alunos
for i in range(10):
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    notas.append(nota)

# a) Calculando a média da turma
media_turma = sum(notas) / len(notas)

# b) Contando quantos alunos estão acima da média
alunos_acima_da_media = len([nota for nota in notas if nota > media_turma])

# c) Encontrando a maior nota
maior_nota = max(notas)

# d) Encontrando as posições em que a maior nota aparece
posicoes_maior_nota = [i for i, nota in enumerate(notas) if nota == maior_nota]

# Exibindo os resultados
print(f"\nA média da turma é: {media_turma:.2f}")
print(f"Quantidade de alunos acima da média: {alunos_acima_da_media}")
print(f"A maior nota digitada foi: {maior_nota}")
print(f"As posições em que a maior nota aparece são: {posicoes_maior_nota}")