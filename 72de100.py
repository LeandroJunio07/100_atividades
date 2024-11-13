# Criando dois vetores, um para múltiplos de 5 e outro para índices de 0 a 9
vetor_multiplos_5 = []
vetor_indices = []

# Preenchendo os vetores conforme a lógica especificada
for i in range(10):
    vetor_multiplos_5.append(5 * (i + 1))  # Preenche com múltiplos de 5
    vetor_indices.append(i)  # Preenche com valores de 0 a 9

# Exibindo os vetores
print("Múltiplos de 5:")
print(vetor_multiplos_5)

print("Índices de 0 a 9:")
print(vetor_indices)