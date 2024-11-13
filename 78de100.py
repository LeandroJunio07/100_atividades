# Criando um vetor vazio para armazenar os números
numeros = []

# Lendo 15 números e armazenando no vetor
for i in range(15):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Mostrando o vetor completo
print("\nVetor completo:")
print(numeros)

# Encontrando e mostrando as posições dos múltiplos de 10
print("\nPosições dos números múltiplos de 10:")
for i, numero in enumerate(numeros):
    if numero % 10 == 0:
        print(f"Índice {i}: {numero}")