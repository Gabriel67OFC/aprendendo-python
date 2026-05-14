n1 = int(input("Digite um numero: "). replace(",", "."))
n2 = int(input("Digite um numero: "). replace(",", "."))

if n1 > n2:
    print("Numero {} é maior que {}".format(n1,n2))

elif n1 < n2:
    print("Numero {} é menor que {}".format(n1,n2))

else:
    print("Os dois números são iguais")