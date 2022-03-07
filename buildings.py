import os
from constants import *
from colorama import init, Fore, Back, Style
import random

init()

"""
Town Hall: Yellow : 1
Huts: Blue : 2
Walls: Magenta : 3
Cannon: red (?) : 4
"""


class Buildings:
    def __init__(this):
        this.buildings = []
        this.a = []
        for i in range(game_ht[1]):
            this.a.append([])
            for j in range(game_wd[1]):
                this.a[i].append(0)

    def generator(this):
        this.hall_generator()
        this.hut_generator()
        this.cannon_generator()

    def wall_generator(this, x):
        w = Wall()
        w.upd_col(this.col - 1)
        w.upd_row(this.row - 1)
        # w.upd_isdestroyed(1)
        if x == 1:
            w.upd_col_size(5)
            w.upd_row_size(6)
        else:
            w.upd_col_size(4)
            w.upd_row_size(4)
        this.buildings.append(w)

    def hall_generator(this):
        this.row = game_ht[1] // 2 - 2
        this.col = int(game_wd[1] / 1.7)
        t = TownHall()
        t.upd_col(this.col)
        t.upd_row(this.row)
        # t.upd_isdestroyed(1)
        this.buildings.append(t)
        this.wall_generator(1)
        r = this.row - 1
        c = this.col - 1
        for i in range(6):
            for j in range(5):
                if i == 0 or i == 5 or j == 0 or j == 4:
                    this.a[r + i][c + j] = 3
                else:
                    this.a[r + i][c + j] = t.ret_type()

    def building_check(this, r, c, x):
        if x == 2:
            for i in range(4):
                for j in range(4):
                    if this.a[r + i][c + j] != 0:
                        return 0
            return 1

        elif x == 4:
            if this.a[r][c] != 0:
                return 0
            else:
                return 1

    def hut_generator(this):
        huts = 5
        while huts > 0:
            this.row = random.randint(2, game_ht[1] // 1.2)
            this.col = random.randint(game_wd[0] + 5, game_wd[1] - 10)
            if this.building_check(this.row - 1, this.col - 1, 2):
                huts -= 1
                h = Hut()
                h.upd_col(this.col)
                h.upd_row(this.row)
                this.buildings.append(h)
                this.wall_generator(2)
                r = this.row - 1
                c = this.col - 1
                for i in range(4):
                    for j in range(4):
                        if i == 0 or i == 3 or j == 0 or j == 3:
                            this.a[r + i][c + j] = 3
                        else:
                            this.a[r + i][c + j] = 2
        return

    def cannon_generator(this):
        cannons = 5
        while cannons > 0:
            this.row = random.randint(2, game_ht[1] // 1.2)
            this.col = random.randint(game_wd[0] + 5, game_wd[1] - 10)
            if this.building_check(this.row, this.col, 4):
                c = Cannon()
                c.upd_col(this.col)
                c.upd_row(this.row)
                this.buildings.append(c)
                cannons -= 1
                this.a[this.row][this.col] = 4
        return

    def show(this, screen, x):
        for i in range(game_ht[1]):
            for j in range(game_wd[1]):
                if this.a[i][j] != 0 and screen[i][j] == " ":
                    screen[i][j] = this.a[i][j]
        for building in this.buildings:
            if building.ret_type() != 3:
                s1 = building.ret_row_size()
                s2 = building.ret_col_size()
                if building.ret_isdestroyed() == 1:
                    for i in range(s1):
                        for j in range(s2):
                            x.append("here")
                            screen[building.ret_row() + i][building.ret_col() + j] = " "

            elif building.ret_type() == 3:
                s1 = building.ret_row_size()
                s2 = building.ret_col_size()
                # x.append('here1')

                if building.ret_isdestroyed() == 1:
                    for i in range(s1):
                        for j in range(s2):
                            if (
                                screen[building.ret_row() + i][building.ret_col() + j]
                                == 3
                            ):
                                screen[building.ret_row() + i][
                                    building.ret_col() + j
                                ] = " "


class Building:
    # Building Object
    def __init__(this):
        this.__health = 0
        this.__type = 0
        this.__row = 0
        this.__col = 0
        this.__isdestroyed = 0
        this.__row_size = 0
        this.__col_size = 0

    def ret_health(this):
        return this.__health

    def upd_health(this, x):
        this.__health = x

    def ret_type(this):
        return this.__type

    def upd_type(this, x):
        this.__type = x

    def ret_row(this):
        return this.__row

    def upd_row(this, x):
        this.__row = x

    def ret_col(this):
        return this.__col

    def upd_col(this, x):
        this.__col = x

    def ret_isdestroyed(this):
        return this.__isdestroyed

    def upd_isdestroyed(this, x):
        this.__isdestroyed = x

    def ret_row_size(this):
        return this.__row_size

    def upd_row_size(this, x):
        this.__row_size = x

    def ret_col_size(this):
        return this.__col_size

    def upd_col_size(this, x):
        this.__col_size = x

    def on_attack(this, damage):
        this.upd_health(this.ret_health() - damage)
        if this.ret_health() <= 0:
            this.upd_isdestroyed(1)
            # os.system("aplay -q ./sounds/explosion.wav &")


class TownHall(Building):
    def __init__(this):
        Building.__init__(this)
        this.upd_type(1)
        this.upd_health(100)
        this.upd_row_size(4)
        this.upd_col_size(3)


class Hut(Building):
    def __init__(this):
        Building.__init__(this)
        this.upd_type(2)
        this.upd_health(50)
        this.upd_row_size(2)
        this.upd_col_size(2)


class Wall(Building):
    def __init__(this):
        Building.__init__(this)
        this.upd_type(3)
        this.upd_health(30)
        this.upd_row_size(1)
        this.upd_col_size(1)


class Cannon(Building):
    def __init__(this):
        Building.__init__(this)
        this.upd_type(4)
        this.upd_health(20)
        this.upd_row_size(1)
        this.upd_col_size(1)
        this.range = 8  # 8 tiles
        this.damage = 5  # 1 shot = 5 health