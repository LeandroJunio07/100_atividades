def Somador(a, b):
    # A função recebe dois parâmetros e retorna a soma entre eles
    return a + b

# Programa principal
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Chamando a função Somador e armazenando o resultado em uma variável
resultado = Somador(numero1, numero2)

# Exibindo o resultado da soma
print(f"A soma entre {numero1} e {numero2} é: {resultado}")