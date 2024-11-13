import random

# Criando o vetor de 30 posições com números aleatórios entre 1 e 15
vetor = [random.randint(1, 15) for _ in range(30)]

# Exibindo o vetor gerado (opcional)
print("Vetor gerado:", vetor)

# Solicitando ao usuário a chave que deseja procurar
chave = int(input("Digite um número entre 1 e 15 para procurar: "))

# Inicializando variáveis para contar a quantidade de vezes que a chave aparece
contagem = 0
posicoes = []

# Procurando a chave no vetor
for i, num in enumerate(vetor):
    if num == chave:
        posicoes.append(i)  # Adiciona a posição ao vetor de posições
        contagem += 1

# Mostrando os resultados
if contagem > 0:
    print(f"A chave {chave} foi encontrada {contagem} vez(es) nas posições: {posicoes}")
else:
    print(f"A chave {chave} não foi encontrada no vetor.")