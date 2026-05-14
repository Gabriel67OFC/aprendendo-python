ano_de_nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_de_nascimento


if idade <= 17:
    print(f"Você tem {idade} anos. Você é menor de idade!")

elif idade >=60:
    print(f"Você tem {idade} anos. Você é idoso")

else:
    print(f"Você tem {idade} anos. Você é maior de idade!")



