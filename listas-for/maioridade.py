maiores = 0
menores = 0

for i in range(7):
    nascimento = int(input(f"Digite o ano de nascimento da {i + 1} pessoa: "))

    idade = 2026 - nascimento

    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print("Quantidade de maiores de idade:", maiores)
print("Quantidade de menores de idade:", menores)