# importando bibliotecals
import os
import datetime
from datetime import date

# entrada de dados
nome = (input("Digite seu nome: "))
idade = (input("Digite sua idade: "))

# laço de repetição
while True:
    # menu
    print(f"{'-' * 20} FILMES EM CARTAZ {'-' * 20}\n")
    print("- Sala 1: A roda Quadrada - Livre")
    print("- Sala 2: A volta dos que Não Foram - 12 anos")
    print("- Sala 3: Poeira em Alto Mar - 14 anos")
    print("- Sala 4: As Tranças do Rei Careca - 16 anos")
    print("- Sala 5: A Vingança do Peixe Frito - 18 anos\n")

    opcao = print(input("Informe o numero da sala desejada: ")).strip()

    match opcao:
        case "1":
            







"""
TODO - atividade: Crie um programa que recebe do usuário o nome e a idade, e em seguida, mostre um menu de filmes com suas respectivas classificações indicativas e
salas de exibição. Exemplo:
- Sala 1: A roda Quadrada - Livre
- Sala 2: A volta dos que Não Foram - 12 anos
- Sala 3: Poeira em Alto Mar - 14 anos
- Sala 4: As Tranças do Rei Careca - 16 anos
- Sala 5: A Vingança do Peixe Frito - 18 anos
O usuário deve escolher a sala que está passando o filme que deseja assistir.
Se o usuário tiver a idade mínima ou mais para ver o filme, o program imprime o ingresso com o nome do usuário, a sala, o nome do filme, a data e a
hora da compra do ingresso, e deseje um bom filme, e em seguida encerra o programa.
- Se o usuário não tiver a idade mínima para ver o filme, o programa bloqueia a sua entrada, e re-exibe o menu de filmes para que ele escolha outro filme.
"""