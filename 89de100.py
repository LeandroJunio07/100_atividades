def Gerador(mensagem, vezes, tipo_borda):
    # Definindo as bordas
    if tipo_borda == 1:
        linha = "+" + "-"*7 + "="*7 + "-"*7 + "+"
    elif tipo_borda == 2:
        linha = "~" * 8 + ":" * 7 + "~" * 8
    elif tipo_borda == 3:
        linha = "<" * 8 + "-" * 7 + ">" * 8
    else:
        print("Tipo de borda inválido!")
        return
    
    # Exibindo a borda superior
    print(linha)
    
    # Exibindo a mensagem repetida "vezes" vezes
    for _ in range(vezes):
        print(f" {mensagem} ")
    
    # Exibindo a borda inferior
    print(linha)

# Exemplo de uso:
Gerador("Portugol Studio", 3, 2)