def Gerador(mensagem):
    # Definindo o tamanho da linha visual
    linha = "+" + "-"*7 + "="*7 + "-"*7 + "+"
    
    # Exibindo a borda superior, a mensagem personalizada e a borda inferior
    print(linha)
    print(f" {mensagem} ")
    print(linha)

# Chamando o procedimento Gerador com uma mensagem personalizada
Gerador("Aprendendo Portugol")