import random

# Preenchendo o vetor de 20 posições com números aleatórios entre 0 e 99
vetor = [random.randint(0, 99) for _ in range(20)]

# Exibindo os números gerados
print("Vetor gerado aleatoriamente:")
print(vetor)

# Ordenando o vetor em ordem crescente
vetor.sort()

# Exibindo o vetor ordenado
print("\nVetor ordenado em ordem crescente:")
print(vetor)