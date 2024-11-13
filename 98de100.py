def SuperSomador(inicio, fim):
    # A função vai somar todos os números no intervalo entre 'inicio' e 'fim'
    soma = 0
    
    # Certificando que o intervalo é percorrido do menor para o maior número
    if inicio > fim:
        inicio, fim = fim, inicio  # Troca os valores para garantir que 'inicio' <= 'fim'
    
    for num in range(inicio, fim + 1):
        soma += num  # Adiciona o número ao somatório
    
    return soma

# Programa principal
inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

# Chamando a função SuperSomador
resultado = SuperSomador(inicio, fim)

# Exibindo o resultado
print(f"A soma de todos os valores no intervalo de {inicio} a {fim} é: {resultado}")