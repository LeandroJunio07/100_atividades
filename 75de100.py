# Criando dois vetores: um para a sequência de Fibonacci e outro para os índices de 0 a 15
fibonacci = []
indices = []

# Preenchendo o vetor da sequência de Fibonacci
a, b = 1, 1  # Iniciando os dois primeiros números da sequência de Fibonacci

for i in range(15):
    fibonacci.append(a)
    a, b = b, a + b  # Atualiza os valores para os próximos termos da sequência

# Preenchendo o vetor de índices (0 a 15)
for i in range(16):
    indices.append(i)

# Exibindo os vetores
print("Sequência de Fibonacci:")
print(fibonacci)

print("Índices (0 a 15):")
print(indices)