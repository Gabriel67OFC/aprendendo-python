nota = -1

while nota < 0 or nota > 10:
    nota = float(input("Digite uma nota de 0 a 10: "))


    if nota < 0 or nota > 10:
        print("Número inválido!")

print("Nota válida!")