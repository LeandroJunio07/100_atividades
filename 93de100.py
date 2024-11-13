def Contador(inicio, fim, incremento):
    # Verificando se o incremento é positivo ou negativo para contar corretamente
    if incremento > 0:
        # Contagem crescente
        for i in range(inicio, fim + 1, incremento):
            print(i, end=' ')
    elif incremento < 0:
        # Contagem decrescente
        for i in range(inicio, fim - 1, incremento):
            print(i, end=' ')
    else:
        print("O incremento não pode ser zero.")

    print()  # Apenas para pular uma linha após a contagem.

# Programa principal
inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))
incremento = int(input("Digite o valor de incremento: "))

# Chamando o procedimento Contador
Contador(inicio, fim, incremento)