import os

class output:
    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")


def level_3():
    cont = 0

    pergunta1 = "1 x 2 = "
    pergunta2 = "2 x 5 = "
    pergunta3 = "2 x 10 = "

    output.clear()

    while True:
        print(pergunta1)
        if input("coloque o resultado ") == "2":
            cont += 1
        else:
            output.clear()
            print("Voce errou")

        print(pergunta2)
        if input("coloque o resultado ") == "10":
            cont += 1
        else:
            output.clear()
            print("Voce errou")

        print(pergunta3)
        if input("coloque o resultado ") == "20":
            cont += 1
        else:
            output.clear()
            print("Voce errou")

        print(f"Voce acertou {cont}")

        if cont == 3:
            output.clear()
            print("Parabens! Voce finalizou todos os levels!")
            break

        elif cont == 2:
            output.clear()
            print("Parabens, voce tirou uma nota media")
            cont = 0

        else:
            output.clear()
            print("Na proxima voce se sai melhor")
            cont = 0
