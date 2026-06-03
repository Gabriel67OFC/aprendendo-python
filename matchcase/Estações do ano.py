mes = input("Digite o nome ou o número do mês: ").strip().lower()

match mes:
    case "12" | "dezembro" | "1" | "janeiro" | "2" | "fevereiro":
        print("Verão")

    case "3" | "março" | "marco" | "4" | "abril" | "5" | "maio":
        print("Outono")

    case "6" | "junho" | "7" | "julho" | "8" | "agosto":
        print("Inverno")

    case "9" | "setembro" | "10" | "outubro" | "11" | "novembro":
        print("Primavera")

    case _:
        print("Mês inválido!")