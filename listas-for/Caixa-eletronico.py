valor = int(input('Digite o valor do saque R$: '))

cedulas = (50,20,10,5,2)

for cedula in cedulas:
    quantidade = valor // cedula

if quantidade > 0:
    print(f"{quantidade} cédula(s) de R$ {cedula}")

    valor = valor % cedula

if valor != 0:
    print("Não foi possível sacar o valor exato.")
