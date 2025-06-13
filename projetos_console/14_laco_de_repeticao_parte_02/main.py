# Loop infinito
while True:
    # menu
    print(f"{'-' * 20} MENU {'-' * 20}")
    print("0 - Encerrar o programa")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    operador = input("Informe a opção desejada: ").strip()
    # Verifica a opção escolhida
    match operador:
        case "0":
            print("Progama encerrado.")
            break  # Encerra o loop e o programa
        case "1":
            try:
                x = float(input("Informe o valor de X:").replace(",", "."))
                y = float(input("Informe o valor de Y:").replace(",", "."))

                print(f"{x} + {y} = {x+y}")
            except Exception as e:
                print(f"Não foi possível subtrair. {e}." )
            finally:
                continue  # Continua para o próximo loop
        case "2":
            try:
                x = float(input("Informe o valor de X:").replace(",", "."))
                y = float(input("Informe o valor de Y:").replace(",", "."))

                print(f"{x} - {y} = {x-y}")
            except Exception as e:
                print(f"Não foi possível subtrair. {e}." )
            finally:
                continue  # Continua para o próximo loop
        case "3":
            try:
                x = float(input("Informe o valor de X:").replace(",", "."))
                y = float(input("Informe o valor de Y:").replace(",", "."))

                print(f"{x} * {y} = {x*y}")
            except Exception as e:
                print(f"Não foi possível multiplicar. {e}." )
            finally:
                continue  # Continua para o próximo loop
        case "4":
            try:
                x = float(input("Informe o valor de X:").replace(",", "."))
                y = float(input("Informe o valor de Y:").replace(",", "."))

                print(f"{x} / {y} = {x/y}")
            except Exception as e:
                print(f"Não foi possível dividir. {e}." )
            finally:
                continue  # Continua para o próximo loop
        case _:
            print("Operador inválido")  # Caso não seja nenhuma das opções, não faz nada
            continue  # Continua para o próximo loop