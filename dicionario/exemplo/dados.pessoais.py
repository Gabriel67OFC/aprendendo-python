from email.policy import default

dados_pessoais = {

    "nome" : "João",
    "idade": 21,
    "nascimento" : "20-05-2005",
    "sexo" : "M",
    "altura": 1.70,
    "temCNH": True
}

continuar = "s"
while continuar == "s":


    dados = input("Digite o voce quer encontrar: ")

    print(dados_pessoais.get(dados, "Valor não encontrado!"))
    break