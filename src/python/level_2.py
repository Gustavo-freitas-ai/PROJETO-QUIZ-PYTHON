import os
import level_1
from level_3 import level_3

class output:
    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")


def level_2():
    cont = 0

    pergunta1 = "1 x 1 = "
    pergunta2 = "2 x 4 = "
    pergunta3 = "3 x 6 = "

    output.clear()

    while True:
        print(pergunta1)
        if input("coloque o resultado ") == "1":
            cont += 1
        else:
            output.clear()
            print("Voce errou")

        print(pergunta2)
        if input("coloque o resultado ") == "8":
            cont += 1
        else:
            output.clear()
            print("Voce errou")

        print(pergunta3)
        if input("coloque o resultado ") == "18":
            cont += 1
        else:
            output.clear()
            print("Voce errou")

        print(f"Voce acertou {cont}")

        if cont == 3:
            level_1.lvl = 2
            output.clear()
            escolha = input("""
Parabens, voce tirou a nota maxima!
Deseja continuar para o level 3?

[1] sim
[2] nao
""")
            if escolha == "1":
                level_3()
            break

        elif cont == 2:
            output.clear()
            print("Parabens, voce tirou uma nota media")
            cont = 0

        else:
            output.clear()
            print("Na proxima voce se sai melhor")
            cont = 0
