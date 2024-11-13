def Media(nota1, nota2):
    # A função calcula a média entre as duas notas e retorna o resultado
    return (nota1 + nota2) / 2

# Programa principal
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

# Chamando a função Media e armazenando o resultado em uma variável
resultado_media = Media(nota1, nota2)

# Exibindo a média
print(f"A média do aluno é: {resultado_media:.2f}")