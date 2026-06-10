matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

numero = int(input("Digite o número: "))

encontrado = False

for linha in range(3):
    for coluna in range(3):
        if matriz[linha][coluna] == numero:
            print(f"Número encontrado na linha {linha} e coluna {coluna}")
            encontrado = True

if not encontrado:
    print("Número não encontrado")