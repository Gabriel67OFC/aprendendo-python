matriz_base = [[12,2], [5,8]]

fator = int(input("Digite o fator: "))

for linha in matriz_base:
    print([linha[0] * fator, linha[1] * fator])