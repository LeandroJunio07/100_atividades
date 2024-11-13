def Maior(a, b, c):
    # Função que recebe três números e retorna o maior
    return max(a, b, c)

# Programa principal
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Chamando a função Maior para obter o maior número entre os três
resultado = Maior(numero1, numero2, numero3)

# Exibindo o maior número
print(f"O maior número entre {numero1}, {numero2} e {numero3} é: {resultado}")