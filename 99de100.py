def Potencia(base, expoente):
    # A função calcula a potência (base^expoente) e retorna o resultado
    return base ** expoente

# Programa principal
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

# Chamando a função Potencia e armazenando o resultado
resultado = Potencia(base, expoente)

# Exibindo o resultado da exponenciação
print(f"O resultado de {base} elevado a {expoente} é: {resultado}")