numeros = []
for i in range(6):
    num = int(input(f"Digite o {i+1} número: "))
    numeros.append(num)

print("Lista completa: ", numeros)
print("Soma dos valores: ", sum(numeros))
print("Maior valor: ", max(numeros))
print("Menor valor: ", min(numeros))