perfil = input("Digite o perfil do usuário: ").upper()

match perfil:
    case "ADMIN":
        print("Acesso total: Criar, Ler, Atualizar e Deletar.")

    case "GERENTE":
        print("Acesso gerencial: Criar, Ler e Atualizar.")

    case "EDITOR":
        print("Acesso de conteúdo: Ler e Atualizar.")

    case "VISITANTE":
        print("Acesso básico: Apenas Ler.")

    case _:
        print("Perfil não reconhecido. Acesso bloqueado.")