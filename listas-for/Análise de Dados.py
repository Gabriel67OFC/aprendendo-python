idade = 0
homens = 0
mulheres_menos20 = 0

while True:
    idade = int(input("Digite a sua idade: "))
    sexo = input("Digite o seu sexo [M/F]: ").upper()

    if idade > 18:
        print("Maior de idade")

    if sexo == "M":
        print("Homem")
        homens += 1

    if sexo == "F":
        print("Mulher")

    if sexo == "F" and idade < 20:
        print("Mulher com menos de 20 anos")
        mulheres_menos20 += 1

    continuar = input("Quer continuar? [S/N]: ").upper()

    if continuar == "N":
        break