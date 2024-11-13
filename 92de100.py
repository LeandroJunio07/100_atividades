def ParOuImpar(numero):
    # Verificando se o número é par ou ímpar
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")

# Lendo o número fornecido pelo usuário
numero = int(input("Digite um número inteiro: "))

# Chamando o procedimento ParOuImpar para verificar e mostrar o resultado
ParOuImpar(numero)