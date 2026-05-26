
Nota = float(input("Informe quantos dias o aluno compareceu as aulas: "))

if frequencia > 0:
    print("Não reprovou por falta")

    n1 = float(input("Digite a primeita nota").replace(",", "."))
    n2 = float(input("Digite a segunda nota").replace (",", "."))

    media = (n1 + n2)/2
    if media>=7: 
        print("aprovado")
    elif media>=5:
        print("Ficou de recuperação")
else: 
    print("Reprovado por falta")

    