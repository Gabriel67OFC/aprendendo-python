senhacerta = 'Cleiton do Grau2026'

for i in range (4):
    senha = input("Digite a sua senha: ")

    if senha == senhacerta:
        print("Bem vindo!")
        break

else:
    print("Senha incorreta!")
