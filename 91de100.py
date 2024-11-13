def Maior(a, b):
    # Verificando qual valor é o maior
    if a > b:
        print(f"O maior valor é: {a}")
    elif b > a:
        print(f"O maior valor é: {b}")
    else:
        print("Os dois valores são iguais.")

# Lendo os valores fornecidos pelo usuário
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Chamando o procedimento Maior para verificar e mostrar o maior valor
Maior(valor1, valor2)