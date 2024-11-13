# Criando um vetor vazio para armazenar os números
numeros = []

# Lendo 10 números e armazenando no vetor
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Mostrando os números pares e suas posições
print("\nNúmeros pares e suas posições:")

# Percorrendo o vetor para verificar quais números são pares
for i, numero in enumerate(numeros):
    if numero % 2 == 0:
        print(f"Número {numero} na posição {i}")