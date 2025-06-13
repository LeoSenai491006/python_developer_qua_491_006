"""
# TODO - atividade:
#  Crie um programa que receba do usuário o valor do etanol e da gasolina em reais, e informe para o usuário qual o melhor combustível para abastecer.
# NOTE - o usuário poderá informar várias vezes os valores, e irá encerrar o programa quando desejar.
# NOTE - cálculo: compensa etanol caso ele tenha até 70% do valor da gasolina.
# NOTE - DIVIRTAM-SE!!! =D
"""

while True:
    etanol = float(input("Informe o valor do etanol: R$ ").replace(',', '.'))
    gasolina = float(input("Informe o valor da gasolina: R$ ").replace(',', '.'))
    if etanol <= 0 or gasolina <= 0:
        print("Valores inválidos. Por favor, informe valores positivos.")
        continue
    if etanol / gasolina <= 0.7:
        print("Compensa abastecer com etanol.")
    else:
        print("Compensa abastecer com gasolina.")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        print("Programa encerrado.")
        break