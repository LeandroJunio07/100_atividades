# Solicita a distância em metros ao usuário
metros = float(input("Digite uma distância em metros: "))
# Calcula as conversões
km = metros / 1000           # Quilômetros
hm = metros / 100            # Hectômetros
dam = metros / 10            # Decâmetros
dm = metros * 10             # Decímetros
cm = metros * 100            # Centímetros
mm = metros * 1000           # Milímetros
# Exibe os resultados
print(f"A distância de {metros}m corresponde a:")
print(f"{km}Km")
print(f"{hm}Hm")
print(f"{dam}Dam")
print(f"{dm}dm")
print(f"{cm}cm")
print(f"{mm}mm")
