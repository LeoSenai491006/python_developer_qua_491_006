# bibliotecas
import os
import random

# lista
nomes = []

while True:
    print("1 - Inserir nome na lista")
    print("2 - Exibir lista")
    print("3 - Sortear nome")
    print("4 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            try:
                novo_nome = input("Informe o nome: ").title().strip()
                os.system("cls" if os.name == "nt" else "clear")
                nomes.append(novo_nome)
                print("Nome inserido com sucesso!")
            except Exception as e:
                print(f"Não foi possível inserir o nome na lista. {e}.")
            finally:
                continue
        case "2":
            try:
                nomes.sort()  # ordenar a lista
                for nome in nomes: # exibe a lista
                    print(nome)
                print('-'*40)
            except Exception as e:
                print(f"Não foi possível exibir lista. {e}")
            finally:
                continue
        case "3":
            i = random.randint(0, len(nomes) - 1)
            print(f"Nome sorteado: {nomes[i]}")
        case "4":
            print("Progama encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue