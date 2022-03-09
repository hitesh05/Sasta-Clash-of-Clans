import os
from src.screen import *
from src.constants import *
from src.background import *
from src.buildings import *
from src.king import *
from src.barbarians import *
from src.spells import *
from src.input import *
import time


os.system("clear")

# setting area of screen where game will be played
comp_screen = Screen(s_height, s_width)

# making a boundary for the village
background = Background()

# creating instance for Buildings class
buildings = Buildings()

# creating instance for King class
king = King()

# creating instance for Spells class
spells = Spells()

# creating 1st barbarian
barbarian1 = Barbarians()
barbarian1.upd_col(game_wd[0] + 1)

# creating 2nd barbarian
barbarian2 = Barbarians()
barbarian2.upd_col(game_wd[0] + 11)

# creating 3rd barbarian
barbarian3 = Barbarians()
barbarian3.upd_col(game_wd[0] + 21)

get = Get()
start_time = time.time()
render_time = time.time()
collapeseTime = time.time()
pause = 0
forward = 0
x = []

# generating all the buildings
def generate(buildings):
    buildings.generator()

# for pausing the game 
def toggle_pause(pause):
    return 1 - pause

# checking if the game has ended (king has died or all the buildings have been destroyed)
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

# health bar for the king
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

'''
displaying the screen
i.e all the buildings, king, and barbarians (if they have been activated)
'''   
def display(king, i, dir):
    global active1
    global active2
    global active3
    # x.append(active1)
    background.show(comp_screen.screen)
    buildings.show(comp_screen.screen, x)
    king.show(comp_screen.screen)
    buildings.cannon_attack(
        comp_screen.screen, king, barbarian1, barbarian2, barbarian3
    )
    if active1 == 1:
        barbarian1.predict_path(comp_screen.screen, buildings.buildings)
        barbarian1.show(comp_screen.screen)
    if active2 == 1:
        barbarian2.predict_path(comp_screen.screen, buildings.buildings)
        barbarian2.show(comp_screen.screen)
    if active3 == 1:
        barbarian3.predict_path(comp_screen.screen, buildings.buildings)
        barbarian3.show(comp_screen.screen)
    comp_screen.display(i, dir)
    print("\033[0:0H")  # reposition the cursor

'''
getting input from user and executing the commands
'''
def get_input(pause, forward):
    global active1
    global active2
    global active3
    ch = input_to(get, frametransition) 
    x.append(active1)

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
        active1 = 1
        barbarian1.upd_active(active1)
    if ch == "m":
        barbarian2.show(comp_screen.screen)
        active2 = 1
        barbarian2.upd_active(active2)
    if ch == "n":
        barbarian3.show(comp_screen.screen)
        active3 = 1
        barbarian3.upd_active(active3)
    if ch == "r":
        spells.spell(barbarian1, barbarian2, barbarian3, king)
    if ch == "h":
        spells.spell(barbarian1, barbarian2, barbarian3, king, 1)
    if ch == "q":
        over(buildings.buildings, x, 0)

    return pause, forward

# main function
if __name__ == "__main__":
    generate(buildings)
    
    # commands for replay
    i = 0
    path = "replays/"
    dir = len(os.listdir(path))
    dir += 1
    command = "mkdir replays/" + str(dir)
    os.system(command)
    
    # checking if barbarians are active
    global active1
    active1 = 0
    global active2
    active2 = 0
    global active3
    active3 = 0
    
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

            display(king, i, dir)
            display_healthbar(king.ret_health(), king.ret_total_health(), 20)
            render_time = time.time()

