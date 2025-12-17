import os

class output:
    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")


def level_2():
    cont = 0

    pergunta1 = "1 x 1 = "
    pergunta2 = "2 x 4 = "
    pergunta3 = "3 x 6 = "

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
            output.clear()
            print("Parabens, voce finalizou o level 2!")
            break
        else:
            cont = 0
            output.clear()
            print("Tente novamente")
