compra = float(input("Digite o valor da compra R$: "))

if compra <= 100:
    print("Não possui desconto")

elif compra >100 and compra <300:
    print("Possui um desconto de 5%")

elif compra >300 and compra <500:
    print("Possui um desconto de 10%")

else:
    print("Possui um desconto de 15%")