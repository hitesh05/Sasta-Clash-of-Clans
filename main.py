import os
from screen import *
from constants import *
from background import *
from buildings import *
from king import *
from barbarians import *
from input import *
import time


os.system("clear")

comp_screen = Screen(s_height, s_width)
background = Background()
buildings = Buildings()
king = King()
barbarian1 = Barbarians()
barbarian1.upd_col(game_wd[0]+1)
barbarian2 = Barbarians()
barbarian2.upd_col(game_wd[0]+11)
barbarian3 = Barbarians()
barbarian3.upd_col(game_wd[0]+21)
get = Get()
start_time = time.time()
render_time = time.time()
collapeseTime = time.time()
pause = 0
forward = 0
x = []


def generate(buildings):
    buildings.generator()


def check_end(king, buildings):
    result = 0
    end = 0
    if king.ret_isdead():
        end = 1
        result = 0
        return end, result
    for i in buildings:
        if i.ret_isdestroyed() == 0:
            return end, result

    end = 1
    result = 1
    return end, result


def display_healthbar(health, maxHealth, healthDashes):
    dashConvert = int(
        maxHealth / healthDashes
    )  # Get the number to divide by to convert health to dashes (being 10)
    currentDashes = int(
        health / dashConvert
    )  # Convert health to dash count: 80/10 => 8 dashes
    remainingHealth = (
        healthDashes - currentDashes
    )  # Get the health remaining to fill as space => 12 spaces

    healthDisplay = "-" * currentDashes  # Convert dashes as a string:   "--------"
    remainingDisplay = (
        " " * remainingHealth
    )  # Convert spaces as a string: "            "
    percent = (
        str(int((health / maxHealth) * 100)) + "%"
    )  # Get the percent as a whole number:   40%

    print("|" + healthDisplay + remainingDisplay + "|")  # Print out textbased healthbar
    print("         " + percent)


def display(king,i,dir):
    background.show(comp_screen.screen)
    buildings.show(comp_screen.screen, x)
    king.show(comp_screen.screen)
    comp_screen.display(i,dir)
    print("\033[0:0H")  # reposition the cursor


def toggle_pause(pause):
    return 1 - pause


def get_input(pause, forward):
    ch = input_to(get, frametransition)

    if ch == "w":
        king.move_up(comp_screen.screen)
    if ch == "a":
        king.move_left(comp_screen.screen)
    if ch == "s":
        king.move_down(comp_screen.screen)
    if ch == "d":
        king.move_right(comp_screen.screen)
    if ch == "p":
        return (toggle_pause(pause), forward)
    if ch == " ":
        king.attack(comp_screen.screen, buildings.buildings)
    if ch == "l":
        barbarian1.show(comp_screen.screen)
    if ch == "m":
        barbarian2.show(comp_screen.screen)
    if ch == "n":
        barbarian3.show(comp_screen.screen)
    if ch == "q":
        over(buildings.buildings, x, 0)

    return pause, forward


generate(buildings)
i = 0
path = 'replays/'
dir = len(os.listdir(path))
dir+=1
command = 'mkdir replays/'+str(dir)
os.system(command)
while True:
    i += 1
    pause, forward = get_input(pause, forward)

    if forward == 1:
        forward = 0
        pause = 1
    while pause:
        pause, forward = get_input(pause, forward)

    if time.time() - render_time >= frametransition:
        end, result = check_end(king, buildings.buildings)
        if end:
            over(buildings.buildings, x, result)

        display(king,i,dir)
        display_healthbar(king.ret_health(), king.ret_total_health(), 20)
        render_time = time.time()

