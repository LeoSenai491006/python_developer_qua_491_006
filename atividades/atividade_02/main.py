"""
# TODO - atividade: Crie um programa que receba do usuário, o nome, o peso em kg, e a altura em metros, e calcule o valor do IMC (Indice de Massa Corporal).
O Programa deve mostrar o valor do IMC arredondado para 2 casas decimais, e mostrar o diagnóstico do usuário com base nos seguintes valores:
- Caso o IMC seja menor que 18.5 - abaixo do peso
- Caso o IMC seja maior ou igual a 18.5 e menor que 25 - peso ideal.
- Caso o IMC seja maior ou igual a 25 e menor que 30 - acima do peso
- Caso o IMC seja maior ou igual a 30 e menor que 35 - obeso
- Caso o IMC seja maior ou igual a 35 e menor que 40 - obsidade nivel 2.
- Caso o IMC seja maior ou igual a 40 - obesidade mórbida.
# NOTE - o usuário deverá informar o encerramento do programa, ou seja, ele poderá repetir o cálculo quantas vezes quiser.
"""

# laço de repetição
while True:
    try
    # menu
    print(f"{'-' * 20} CÁLCULO DE IMC {'-' * 20}")
    nome = input("Informe seu nome: ")
    peso = float(input("Informe seu peso: (em kg): ").replace(",","."))
    altura = float(input("Infome sua altura: (em metros): ").replace(",","."))

    imc = peso / (altura ** 2)

    # Definindo a categoria com base no IMC
    if imc < 18.5:
        categoria = "abaixo"
    elif imc < 25:
        categoria = "ideal"
    elif imc < 30:
        categoria = "acima"
    elif imc < 35:
        categoria = "obeso1"
    elif imc < 40:
        categoria = "obeso2"
    else:
        categoria = "obesidade_morbida"
    
    
    # Usando match case
    match categoria:
        case "abaixo":
            diagnostico = "Abaixo do peso"
        case "ideal":
            diagnostico = "Peso ideal"
        case "acima":
            diagnostico = "Acima do peso"
        case "obeso1":
            diagnostico = "Obeso"
        case "obeso2":
            diagnostico = "Obesidade nível 2"
        case "obesidade_morbida":
            diagnostico = "Obesidade mórbida"
    
    print(f"{nome}, seu IMC é: ")
