# Criando dois vetores, um para a alternância entre 5 e 3, e outro para os índices de 0 a 9
vetor_alternado = []
vetor_indices = []

# Preenchendo os vetores conforme a lógica
for i in range(10):
    if i % 2 == 0:
        vetor_alternado.append(5)  # Posições pares (0, 2, 4...) recebe 5
    else:
        vetor_alternado.append(3)  # Posições ímpares (1, 3, 5...) recebe 3
    
    vetor_indices.append(i)  # Preenche com números de 0 a 9

# Exibindo os vetores
print("Vetor alternado (5 e 3):")
print(vetor_alternado)

print("Vetor de índices (0 a 9):")
print(vetor_indices)