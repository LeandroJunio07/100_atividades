import random

# Criando um vetor vazio para armazenar os números aleatórios
vetor_aleatorio = []

# Preenchendo o vetor com 7 números aleatórios entre 1 e 100 (por exemplo)
for _ in range(7):
    numero = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
    vetor_aleatorio.append(numero)

# Exibindo os valores gerados
print("Números gerados aleatoriamente:")
print(vetor_aleatorio)