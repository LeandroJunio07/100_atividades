# Solicita a quantidade de dinheiro em reais ao usuário
reais = float(input("Quanto dinheiro você tem na carteira (em R$): "))
# Conversão para dólares
dolares = reais / 3.45
# Exibe o resultado
print(f"Com R${reais:.2f}, você pode comprar US${dolares:.2f}.")