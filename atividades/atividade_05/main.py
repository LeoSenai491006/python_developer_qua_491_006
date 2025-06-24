# importando bibliotecas
import os
import datetime
from datetime import date

# função para limpar a tela
def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")

# entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# laço de repetição
while True:
    # menu
    print(f"{'-' * 20} FILMES EM CARTAZ {'-' * 20}\n")
    print("- Sala 1: A roda Quadrada - Livre")
    print("- Sala 2: A volta dos que Não Foram - 12 anos")
    print("- Sala 3: Poeira em Alto Mar - 14 anos")
    print("- Sala 4: As Tranças do Rei Careca - 16 anos")
    print("- Sala 5: A Vingança do Peixe Frito - 18 anos\n")

    opcao = input("Informe o número da sala desejada: ").strip()
    data = date.today().strftime("%d/%m/%Y")
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    hora_data = f"{hora} - {data}\n"

    match opcao:
        case "1":
            print(f"\nINGRESSO para {nome}.\n")
            print("Sala 1: A roda Quadrada.")
            print(hora_data)
            print("Tenha um bom filme.")
            break
        case "2":
            if idade >= 12:
                print(f"\nINGRESSO para {nome}.\n")
                print("Sala 2: A volta dos que Não Foram.")
                print(hora_data)
                print("Tenha um bom filme.")
                break
            else:
                print("\nEntrada bloqueada devido à classificação indicativa. Escolha outro filme.")
                input("Pressione ENTER para continuar...")
                limpa_tela()
        case "3":
            if idade >= 14:
                print(f"\nINGRESSO para {nome}.\n")
                print("Sala 3: Poeira em Alto Mar.")
                print(hora_data)
                print("Tenha um bom filme.")
                break
            else:
                print("\nEntrada bloqueada devido à classificação indicativa. Escolha outro filme.")
                input("Pressione ENTER para continuar...")
                limpa_tela()
        case "4":
            if idade >= 16:
                print(f"\nINGRESSO para {nome}.\n")
                print("Sala 4: As Tranças do Rei Careca.")
                print(hora_data)
                print("Tenha um bom filme.")
                break
            else:
                print("\nEntrada bloqueada devido à classificação indicativa. Escolha outro filme.")
                input("Pressione ENTER para continuar...")
                limpa_tela()
        case "5":
            if idade >= 18:
                print(f"\nINGRESSO para {nome}.\n")
                print("Sala 5: A Vingança do Peixe Frito.")
                print(hora_data)
                print("Tenha um bom filme.")
                break
            else:
                print("\nEntrada bloqueada devido à classificação indicativa. Escolha outro filme.")
                input("Pressione ENTER para continuar...")
                limpa_tela()
        case _:
            print("\nOpção inválida. Tente novamente.")
            input("Pressione ENTER para continuar...")
            limpa_tela()