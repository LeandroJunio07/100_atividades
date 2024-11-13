def Gerador(mensagem, vezes):
    # Definindo o tamanho da linha visual
    linha = "+" + "-"*7 + "="*7 + "-"*7 + "+"
    
    # Exibindo a borda superior
    print(linha)
    
    # Exibindo a mensagem repetida "vezes" vezes
    for _ in range(vezes):
        print(f" {mensagem} ")
    
    # Exibindo a borda inferior
    print(linha)

# Chamando o procedimento Gerador com uma mensagem personalizada e repetindo 4 vezes
Gerador("Aprendendo Portugol", 4)