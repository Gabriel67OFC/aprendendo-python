n1 = int(input("Digite o primeiro numero"))
n2 = int(input("Digite o segundo numero"))

resultado = n1 // n2
resultado = n1 % n2
resultado = n1 ** n2

print ("O resultado da parte inteira da divisão é :", resultado)
print ("O resultado do resto da divisão é :", resultado)
print ("O resultado da potencia é :", resultado)

print("---------------------------------------")
print(" OPERADORES RELACIONAIS")
print("---------------------------------------")


relacao1 = n1 > n2
relacao2 = n1 < n2
relacao3 = n1 >= n2
relacao4 = n1 <= n2
relacao5 = n1 == n2
relacao6 = n1 != n2

print ("Os resultados das relacoes estarao abaixo: \n{} \n{} \n{} \n{} \n{} \n{} ".format(relacao1, relacao2, relacao3, relacao4, relacao5, relacao6))