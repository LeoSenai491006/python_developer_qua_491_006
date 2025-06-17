# importando biblioteca
import math as m # "apelidando" a biblioteca de m

# exibe o número de pi
print(f"Número do pi: {m.pi}.")

# raiz quadrada

try:
    n = int(input("Informe um número inteiro: "))
    print(f"A raiz quadrada de {n} é {m.sqrt(n):.2f}.") # m.sqrt é o comando para calcular a raiz quadrada
except Exception as e:
    print(f"Não foi possível calcular a raíz quadrada. {e}.")