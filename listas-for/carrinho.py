carrinho = []

while True:
    produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")

    if produto.lower() == "sair":
        break

    carrinho.append(produto)

print("\n===== CARRINHO DE COMPRAS =====")


for item in sorted(carrinho):
    print(item)

