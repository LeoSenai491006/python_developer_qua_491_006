# declaração de variáveis
x = float(input("Informe o valor de X: ").replace(",", "."))
y = float(input("Informe o valor de Y: ").replace(",", "."))

# menu
print(f"\n{'-'*20} ESCOLHA A OPERAÇÃO {'-'*20}\n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# usuário escolhe a operação desejada
operador = input("Informe a operação desejada: ").strip() #.strip() = elimina valores nulos antes é depois.


# match case
match operador:
    case "1":
        print(f"A soma dos valores é {x+y}.")
    case "2":
        print(f"A subtração dos valores é {x-y}.")
    case "3":
        print(f"A multiplicação dos valores é {x*y}.")
    case "4":
        if y != 0:
            print(f"A divisão dos valores é {x/y}.")
        else:
            print("Não é possível dividir por zero.")
    case _: # default (caso não escolha nenhuma das opções acima)
        print("Operação inválida")