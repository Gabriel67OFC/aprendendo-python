numeros = []
pares = []
impares = []

for i in range(10):
    numero = int(input(f"Digite o {i+1} número: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista principal: ", numeros)
print("Lista de pares: ", pares)
print("Lista de ímpares: ", impares)