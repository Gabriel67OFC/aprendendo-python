while True:
    print("\n===== CALCULADORA =====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Encerrando o sistema...")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        resultado = num1 + num2
        print("Resultado:", resultado)

    elif opcao == "2":
        resultado = num1 - num2
        print("Resultado:", resultado)

    elif opcao == "3":
        resultado = num1 * num2
        print("Resultado:", resultado)

    elif opcao == "4":
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Não é possível dividir por zero!")

    else:
        print("Opção inválida!")