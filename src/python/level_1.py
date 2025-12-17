import os
import time
from level_2 import level_2

class output:
    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")


lvl = 0


def level_1():
    global lvl
    cont = 0

    pergunta1 = "1 + 1 = "
    pergunta2 = "2 + 2 = "
    pergunta3 = "3 + 3 = "

    output.clear()

    while True:
        print(pergunta1)
        if input("coloque o resultado ") == "2":
            cont += 1
        else:
            output.clear()
            print("Voce errou")

        print(pergunta2)
        if input("coloque o resultado ") == "4":
            cont += 1
        else:
            output.clear()
            print("Voce errou")

        print(pergunta3)
        if input("coloque o resultado ") == "6":
            cont += 1
        else:
            output.clear()
            print("Voce errou")

        print(f"Voce acertou {cont}")

        if cont == 3:
            lvl = 1
            output.clear()
            escolha = input("""
Parabens, voce tirou a nota maxima!
Deseja continuar para o level 2?

[1] sim
[2] nao
""")
            if escolha == "1":
                level_2()
            break

        elif cont == 2:
            output.clear()
            print("Parabens, voce tirou uma nota media")
            cont = 0

        else:
            output.clear()
            print("Na proxima voce se sai melhor")
            cont = 0
