def Fibonacci(n):
    # Inicializando os dois primeiros termos da sequência de Fibonacci
    a, b = 0, 1
    
    print("Sequência de Fibonacci:")
    
    # Gerando e exibindo os termos da sequência
    for i in range(n):
        print(a, end=' ')
        # Atualizando os valores de a e b para os próximos termos
        a, b = b, a + b
    
    print()  # Quebra de linha ao final

# Programa principal
n = int(input("Digite o número de termos da sequência de Fibonacci: "))

# Chamando o procedimento Fibonacci passando o número de termos
Fibonacci(n)