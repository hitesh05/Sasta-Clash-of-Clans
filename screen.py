from constants import *
from colorama import init, Fore, Back, Style

init()


class Screen:
    def __init__(this, rows, cols):
        this.cols = cols
        this.rows = rows
        this.screen = []

        for i in range(this.rows):
            this.screen.append([])
            for j in range(this.cols):
                this.screen[i].append(" ")

    def display(this,iter,dir):
        name = str(iter)
        dir = str(dir)
        f = open('replays/'+dir+'/'+name,'w')
        for i in range(this.rows):
            for j in range(this.cols):
                tobeprinted = this.screen[i][j]
                if tobeprinted == 1:
                    print(Back.YELLOW + " " + Style.RESET_ALL, end="")
                    f.write(str(Back.YELLOW + " " + Style.RESET_ALL))
                elif tobeprinted == 2:
                    print(Back.BLUE + " " + Style.RESET_ALL, end="")
                    f.write(str(Back.BLUE + " " + Style.RESET_ALL))
                elif tobeprinted == 3:
                    print(Back.MAGENTA + " " + Style.RESET_ALL, end="")
                    f.write(str(Back.MAGENTA + " " + Style.RESET_ALL))
                elif tobeprinted == 4:
                    print(Back.RED + " " + Style.RESET_ALL, end="")
                    f.write(str(Back.RED + " " + Style.RESET_ALL))
                else:
                    print(tobeprinted, end="")
                    f.write(str(tobeprinted))
        f.close()
        
        

