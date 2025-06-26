notas = []

while True:
    try:
        entrada = input("Digite uma nota de 0 a 10 (ou 'sair' para finalizar): ").strip().lower()
        
        if entrada == "sair":
            break 

        nota = float(entrada) 
        
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um número entre 0 e 10.")
            
    except Exception as e:
        print(f"Dados inválidos. {e}")

# Cálculo da média
if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia das notas: {media:.2f}")

    if media >= 7:
        print("Foi aprovado.")
    elif media >= 5:
        print("Ficou de recuperação.")
    else:
        print("Foi reprovado.")
else:
    print("Nenhuma nota foi informada.")

"""
# TODO - atividade: Crie um programa que receba de um professor várias notas de um aluno de 0 a 10 (não importa quantas notas). Ao final do programa,
a média das notas deverá ser calculada e informada, e em seguida, o programa irá informar se o aluno:
- Foi aprovado, caso a média for maior ou igual a 7
- Ficou de recuperação, caso média for entre 5 e 7
- Foi repovado, caso a média for menor que 5.
"""