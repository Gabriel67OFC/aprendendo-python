matriz = [
    [5, 10],
    [3, 2]
]

soma = sum(sum(linha) for linha in matriz)

print(soma)