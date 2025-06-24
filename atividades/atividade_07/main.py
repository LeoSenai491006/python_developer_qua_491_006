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
        print("Nome cadastrado com sucesso!")

    elif opcao == "2":
        for i in range(len(nomes)):
            print(f"{i}: {nomes[i]}.")
    
    elif opcao == "3":
        nome = input("Digite o nome a ser pesquisado: ").title().strip()
        if nome in nomes:
            print(f"{nome} está na lista!")
        else:
            print(f"{nome} não foi encontrado.")
    
    elif opcao == "4":
        try:
            ...
        except Exception as e:
            print("Erro ao alterar o nome: {e}.")






"""
# TODO - atividade: Crie um programa que faça as seguinte operações:
- Cadastre novo nome na lista
- Liste todos os nome da lista
- Pesquise por um nome na lista
- Altere um nome na lista
- Exclua um nome na lista
- Sair do programa
# NOTE - a lista deve começar vazia. Exemplo: lista = []
"""