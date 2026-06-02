while True:
    letra = input("Digite uma letra ou 0 para sair: ").upper()

    match letra:
        case "A"|"E"|"I"|"O"|"U":
            print("Vogal")
        case "0":
            print("Programa encerrado.")
            break
        case:
            print("Consoante")