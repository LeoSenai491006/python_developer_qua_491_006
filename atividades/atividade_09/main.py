# bibliotecas
import os
import datetime
from datetime import date
import random

# lista
usuarios = []

# laço de repetição
while True:
    print(f"{'-' * 20} MENU {'-' * 20}\n")
    print("1 - Cadastre um novo usuário")
    print("2 - Liste todos os usuários")
    print("3 - Altere os dados de um usuário")
    print("4 - Fazer sorteio de usuário")
    print("5 - Exclua um usuário")
    print("6 - Sair")
    opcao = input("\nInforme a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            try:
                nome = input("Informe o nome completo: ").strip().title()
                nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip().replace(".", "/")
                email = input("Informe o E-mail: ").strip().lower()
                cpf = input("Informe o CPF: ").strip().replace(".", "").replace("-", "")
                telefone = input("Informe o telefone: ").strip().replace(" ", "").replace("-", "")

                # validação de gênero
                while True:
                    genero = input("Informe seu gênero (M) para masculino, (F) para feminino: ").strip().upper()
                    if genero == "M" or genero == "F":
                        break
                    print('Gênero inválido. Digite apenas "M" ou "F".')

                dados = {
                    'nome': nome,
                    'nascimento': nascimento,
                    'email': email,
                    'cpf': cpf,
                    'telefone': telefone,
                    'genero': genero,
                    'hora_cadastro': datetime.datetime.now().strftime("%H:%M:%S"),
                    'data_cadastro': date.today().strftime("%d/%m/%Y")
                }

                usuarios.append(dados)

                print(f"\nUsuário {nome} cadastrado com sucesso!\n")
                input("Pressione Enter para continuar...")
                os.system("cls" if os.name == "nt" else "clear")

            except Exception as e:
                print(f"Não foi possível cadastrar o usuário. Erro: {e}")
            finally:
                continue

        case "2":
            if len(usuarios) == 0:
                print("Nenhum usuário cadastrado.\n")
            else:
                print(f"{'-'*20} LISTA DE USUÁRIOS {'-'*20}")
                for usuario in usuarios:
                    print("-" * 40)
                    for chave, valor in usuario.items():
                        print(f"{chave.capitalize()}: {valor}")
                    print("-" * 40)
            input("\nPressione Enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")

        case "3":
            if len(usuarios) == 0:
                print("Nenhum usuário cadastrado.\n")
            else:
                nome_busca = input("Informe o nome do usuário que deseja alterar: ").strip().title()
                encontrado = False
                for usuario in usuarios:
                    if usuario["nome"] == nome_busca:
                        print("\nUsuário encontrado:\n")
                        for chave, valor in usuario.items():
                            print(f"{chave.capitalize()}: {valor}")
                        print("-" * 40)

                        chave = input("Qual informação deseja alterar? (ex: email, telefone, etc.): ").lower().strip()
                        if chave in usuario:
                            novo_valor = input(f"Informe o novo valor para {chave}: ").strip()
                            if novo_valor != "":
                                usuario[chave] = novo_valor
                                print(f"{chave.capitalize()} alterado com sucesso!\n")
                            else:
                                print("O novo valor não pode ser vazio.")
                        else:
                            print("Campo inválido.")
                        encontrado = True
                        break
                if not encontrado:
                    print("Usuário não encontrado.")
            input("\nPressione Enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")

        case "4":
            if len(usuarios) == 0:
                print("Nenhum usuário cadastrado\n")
            else:
                usuario_sorteado = random.randint(0, len(usuarios) -1)
                sorteado = usuarios[usuario_sorteado]

                print("\nUsuário sorteado:\n")
                print("-" * 40)
                for chave, valor in sorteado.items():
                    print(f"{chave.capitalize()}: {valor}")
                print("-" * 40)
            input("\nPressione Enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")

        case "5":
            if len(usuarios) == 0:
                print("Nenhum usuário cadastrado\n")
            else:
                nome_busca = input("Informe o nome do usuário que deseja excluir: ").strip().title()
                encontrado = False

                for usuario in usuarios:
                    if usuario["nome"] == nome_busca:
                        print("\nUsuário encontrado:")
                        for chave, valor in usuario.items():
                            print(f"{chave.capitalize()}: {valor}")
                        print("-" * 40)

                        confirmacao = input("Deseja realmente excluir este usuário? (S/N): ").strip().upper()
                        if confirmacao == "S":
                            usuarios.remove(usuario)
                            print("Usuário excluído com sucesso.")
                        else:
                            print("Exclusão cancelada.")
                        encontrado = True
                        break

                if encontrado == False:
                    print("Usuário não encontrado.")
            input("\nPressione Enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")


"""
# TODO - atividade: Crie um programa que faça as seguintes funções:
- Cadastre um novo usuário
- Liste todos os usuários cadastrados
- Altere os dados de um usuário
- Fazer sorteio de usuário
- Exclua um usuário
- Saia do programa
# NOTE - dados do usuário:
- Nome completo
- Data de Nascimento
- E-mail
- CPF
- Telefone
- Gênero
- Data do cadastro (pegar do sistema)
- Hora do Cadastro (pegar do sistema)
"""