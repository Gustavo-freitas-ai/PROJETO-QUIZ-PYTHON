from level_1 import level_1, lvl
import os

class output:
    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")


while True:
    escolha = input("""
Escolha o level:
1
[1] level 1
[2] level 2
[0] sair
""")

    if escolha == "1":
        output.clear()
        level_1()

    elif escolha == "2":
        if lvl == 1:
            from level_2 import level_2
            output.clear()
            level_2()
        else:
            output.clear()
            print("voce nao tem acesso")

    elif escolha == "0":
        break
