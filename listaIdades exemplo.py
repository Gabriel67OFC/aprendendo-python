listaIdade = []
for i in range (10):
    idade = int(input("Digite sua idade: "))
    listaIdade.append(idade)

print("----------------------------------------------------")
print("Imprindo idades uma abaixo da outra")
listaIdade.sort()

for i in listaIdade:
    print(i)