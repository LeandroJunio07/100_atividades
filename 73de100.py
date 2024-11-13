# Criando dois vetores, um para a sequência decrescente e outro para a sequência crescente
vetor_decrescente = []
vetor_crescente = []

# Preenchendo os vetores conforme a lógica
for i in range(10):
    vetor_decrescente.append(9 - i)  # Preenche com números de 9 a 0
    vetor_crescente.append(i)        # Preenche com números de 0 a 9

# Exibindo os vetores
print("Vetor decrescente (9 a 0):")
print(vetor_decrescente)

print("Vetor crescente (0 a 9):")
print(vetor_crescente)