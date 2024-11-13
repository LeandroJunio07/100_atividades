def Somador(a, b):
    # Calculando a soma
    soma = a + b
    # Exibindo o resultado
    print(f"A soma entre {a} e {b} é: {soma}")

# Lendo os valores fornecidos pelo usuário
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Chamando o procedimento Somador para calcular e mostrar a soma
Somador(valor1, valor2)