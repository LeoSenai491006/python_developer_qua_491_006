"""
# TODO - atividade: Crie um programa que faça as seguintes operações:
- Calcular área de um círculo
- Calcular tamanho de uma circunferência
- Sair do programa
"""

# importando bibliotecas
import os
import math as m

while True:

    

    # entrada de dados
    print(f"{'-' * 20} MENU {'-' * 20}")
    print("0 - Encerrar o programa")
    print("1 - Calcular área de um círculo")
    print("2 - Calcular tamanho de uma circunferência")
    
    operador = input("Informe a opção desejada: ").strip()

    # Verifica a opção escolhida
    match operador:
        case "0":
            print("Programa encerrado.")
            break  # Encerra o loop e o programa

        case "1":
            try:
                raio = float(input("Informe o raio: ").replace(",", "."))
                area = m.pi * (raio ** 2)
                print(f"A área do círculo com raio {raio} é: {area:.2f}")
            except Exception as e:
                print(f"Não foi possível calcular a área. {e}")
            input("\nPressione ENTER para continuar...")
            os.system("cls" if os.name == "nt" else "clear")

        case "2":
            try:
                raio = float(input("Informe o raio: ").replace(",", "."))
                circunferencia = 2 * m.pi * raio
                print(f"O tamanho da circunferência com raio {raio} é: {circunferencia:.2f}")
            except Exception as e:
                print(f"Não foi possível calcular a circunferência. {e}")
            input("\nPressione ENTER para continuar...")
            os.system("cls" if os.name == "nt" else "clear")

        case _:
            print("Opção inválida. Tente novamente.")