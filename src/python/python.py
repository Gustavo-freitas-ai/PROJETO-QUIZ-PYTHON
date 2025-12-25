import os
import level_1
from level_2 import level_2
from level_3 import level_3


class output:
    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")


while True:
    escolha = input("""
Escolha o level:
[1] level 1
[2] level 2
[3] level 3
[0] sair
""")

    match escolha:
        case "1":
            output.clear()
            level_1.level_1()

        case "2":
            if level_1.lvl >= 1:
                output.clear()
                level_2()
            else:
                output.clear()
                print("Você ainda não liberou o level 2.")

        case "3":
            if level_1.lvl >= 2:
                output.clear()
                level_3()
            else:
                output.clear()
                print("Você ainda não liberou o level 3.")

        case "0":
            break
