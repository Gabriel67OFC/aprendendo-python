salario = float(input("Digite o salário bruto do cliente R$: "))
parcela = float(input("Digite o valor da parcela: "))

limite = salario * 0.3

if parcela <= limite:
    print("Crédito aprovado")


else:
    print("Crédito não aprovado")