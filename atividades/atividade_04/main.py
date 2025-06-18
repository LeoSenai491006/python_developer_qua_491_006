import os
import datetime
import time



try:
    while True:
        hora = datetime.datetime.now().strftime("%H:%M:%S")
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{hora}\n")
        print('Pressione "Ctrl+C" para sair do programa.')
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Relógio encerrado pelo usuário.")


"""
# TODO - atividade: Crie um programa que mostre a hora atual sempre sendo atualizada a cada segundo.
# NOTE - para interromper o programa, use a tecla de atalho Ctrl+C
"""