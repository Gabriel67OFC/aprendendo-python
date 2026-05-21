numeros = []

for i in range(6):
    num = int(input(f"Digite o {i + 1} número: "))
    numeros.append(num)

print("Lista completa:", numeros)
print("Soma dos números:", sum(numeros))
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
