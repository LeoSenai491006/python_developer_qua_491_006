# lista
nomes = []

while True:
    print(f"{'-' * 20} MENU {'-' * 20}\n")
    print("1 - Cadastrar nome")
    print("2 - Listar nomes")
    print("3 - Pesquisar nome")
    print("4 - Alterar nome")
    print("5 - Excluir nome")
    print("6 - Sair do programa\n")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ").title().strip()
        nomes.append(nome)
        print("Nome cadastrado com sucesso!\n")

    elif opcao == "2":
        if len(nomes) == 0:
            print("A lista está vazia.\n")
        else:
            for i in range(len(nomes)):
                print(f"Índice {i}: {nomes[i]}")
            print()

    elif opcao == "3":
        nome_pesquisa = input("Digite o nome que deseja pesquisar: ").title().strip()
        if nome_pesquisa in nomes:
            print(f"Nome encontrado no índice {nomes.index(nome_pesquisa)}.\n")
        else:
            print("Nome não encontrado.\n")

    elif opcao == "4":
        if len(nomes) == 0:
            print("A lista está vazia. Nada para alterar.\n")
        else:
            for i in range(len(nomes)):
                print(f"Índice {i}: {nomes[i]}")
            try:
                indice = int(input("Informe o índice do nome a ser alterado: "))
                if indice >= 0 and indice < len(nomes):
                    novo_nome = input("Digite o novo nome: ").title().strip()
                    nomes[indice] = novo_nome
                    print("Nome alterado com sucesso!\n")
                else:
                    print("Índice inválido.\n")
            except Exception as e:
                print(f"Ocorreu um erro: {e}\n")

    elif opcao == "5":
        if len(nomes) == 0:
            print("A lista está vazia. Nada para excluir.\n")
        else:
            for i in range(len(nomes)):
                print(f"Índice {i}: {nomes[i]}")
            try:
                indice = int(input("Informe o índice do nome a ser excluído: "))
                if indice >= 0 and indice < len(nomes):
                    excluido = nomes.pop(indice)
                    print(f"Nome '{excluido}' excluído com sucesso!\n")
                else:
                    print("Índice inválido.\n")
            except Exception as e:
                print(f"Ocorreu um erro: {e}\n")

    elif opcao == "6":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.\n")