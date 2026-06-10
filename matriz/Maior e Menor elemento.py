matriz_valores = [
    [15, 42, 7],
    [23, 91, 12],
    [34, 8, 55]
]

maior = max(max(linha) for linha in matriz_valores)
menor = min(min(linha) for linha in matriz_valores)

for i in range(3):
    for j in range(3):
        if matriz_valores[i][j] == maior:
            print(f"Maior: {maior} na posição [{i}][{j}]")

        if matriz_valores[i][j] == menor:
            print(f"Menor: {menor} na posição [{i}][{j}]")
