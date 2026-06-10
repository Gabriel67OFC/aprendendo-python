matriz_A = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz_T = list(zip(*matriz_A))

for linha in matriz_T:
    print(list(linha))