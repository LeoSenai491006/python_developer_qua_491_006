import json
import os

usuarios = []

while True:
    print(f"\n{'-'*20} MENU {'-'*20}\n")
    print("1 - Criar novo arquivo.")
    print("2 - Informe o diretório que deseja salvar o arquivo.")
    print("3 - Abrir arquivo.")
    print("4 - Cadastrar novo usuário.")
    print("5 - Listar usuários.")
    print("6 - Pesquisar usuário.")
    print("7 - Alterar dados de um usuário.")
    print("8 - Deletar um usuário")
    print("9 - Sair do programa")
    opcao = input("Informe uma opção: ")
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            ...
        case "2":
            ...
        case "3":
            ...
        case "4":

            # TODO - logo após fazer esse cadastro, salvar os dados no arquivo JSON e fazer um try com except

            while True:
                usuario = {}

                usuario['nome'] = input("Informe o nome: ").strip().title()
                usuario['data_nasc'] = input("Informe a data de nascimento: ").strip().replace(".", "/")
                usuario['cpf'] = input("Informe o CPF: ").strip()
                usuario['email'] = input("Informe o e-mail: ").strip().lower()
                usuario['telefone'] = input("Informe o telefone: ").strip()
                usuario['filme'] = input("Informe seu filme favorito: ").strip().title()

                usuarios.append(usuario)
                os.system("cls" if os.name == "nt" else "clear")

            print("Usuário cadastrado com sucesso!")
            continue
        case "5":

            # FIXME - completar o código

            with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
                usuarios = json.load(f)

            print(f"\n{'-'*20} LISTA DE PESSOAS {'-'*20}"\n)
                for usuario in usuarios:
                    print(f"{chave.capitalize()}: {usuario.get(chave)}")
                print("-"*40)
        case "6":
            ...
        case "7":
            ...
        case "8":
            ...
        case "9":
            print("Programa encerrado.\n")
            break
        case _:
            print("Opção inválida.")
            continue

"""
# TODO - atividade: faça um CRUD (Create, Read, Update, Delete) em um JSON.
Opções do menu:
- Criar novo arquivo JSON. (Usuário irá informar o diretório).
- Abrir arquivo JSON.
- Cadastrar novo usuário em um JSON.
- Listar todos os usuários de um arquivo JSON.
- Pesquisar um usuário através do valor de uma chave em um arquivo JSON.
- Alterar dados de um usuário em um arquivo JSON.
- Deletar usuário de um arquivo JSON.
- Sair do programa.
Dados do usuário:
- Nome
- Data de nascimento
- CPF
- E-mail
- Telefone
- Filme favorito do usuário
# NOTE - 
"""