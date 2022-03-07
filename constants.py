import os
from colorama import init, Fore, Back, Style

init()

dims = os.get_terminal_size()
s_height = dims[1]
s_width = dims[0]
game_ht = (0, int(s_height / 1.1))  # height range of game in total screen
# width range of game in total screen
game_wd = (int(s_width / 5), int(s_width - int(s_width / 4)))
frametransition = 0.07


def over(buildings, x, result):
    os.system("clear")
    #     for i in buildings:
    #           t = i.ret_type()
    #           h = i.ret_health()
    #           d = i.ret_isdestroyed()
    #           print(t,h,d)

    print(
        Fore.CYAN
        + Style.BRIGHT
        + "\t\t\t####    ####   ##   ##  ######           ####   ##  ##  ######  ######         "
        + Style.RESET_ALL
    )
    print(
        Fore.CYAN
        + Style.BRIGHT
        + "\t\t\t#      ##  ##  ### ###  ##              ##  ##  ##  ##  ##      ##  ##         "
        + Style.RESET_ALL
    )
    print(
        Fore.CYAN
        + Style.BRIGHT
        + "\t\t\t# ###  ######  ## # ##  ####            ##  ##  ##  ##  ####    #####          "
        + Style.RESET_ALL
    )
    print(
        Fore.CYAN
        + Style.BRIGHT
        + "\t\t\t#  ##  ##  ##  ##   ##  ##              ##  ##   ####   ##      ##  ##         "
        + Style.RESET_ALL
    )
    print(
        Fore.CYAN
        + Style.BRIGHT
        + "\t\t\t####   ##  ##  ##   ##  ######           ####     ##    ######  ##  ##         "
        + Style.RESET_ALL
    )

    if result:
        print(
            Fore.CYAN
            + Style.BRIGHT
            + str("\n\t\t\t\t\t\t\tGAME RESULT: WON\n")
            + Style.RESET_ALL
        )
    else:
        print(
            Fore.CYAN
            + Style.BRIGHT
            + str("\n\t\t\t\t\t\t\tGAME RESULT: LOST\n")
            + Style.RESET_ALL
        )
    quit()
