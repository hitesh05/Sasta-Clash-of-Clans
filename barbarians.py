from constants import *
from colorama import init, Fore, Back, Style

init()

class Barbarians:
    def __init__(this):
        this.__total_health = 20
        this.__health = 20
        this.__isdead = 0
        this.__speed = 1
        this.__damage = 5
        this.__row = game_ht[1] - 2
        this.__col = 0
        this.__is_started = 0
        this.__barbarian = "B"
    
    def ret_total_health(this):
        return this.__total_health
    
    def upd_total_health(this, x):
        this.__health = x
    
    def ret_health(this):
        return this.__health

    def upd_health(this, x):
        this.__health = x

    def ret_row(this):
        return this.__row

    def upd_row(this, x):
        this.__row = x

    def ret_col(this):
        return this.__col

    def upd_col(this, x):
        this.__col = x
        
    def ret_is_started(this):
        return this.__is_started

    def upd_is_started(this, x):
        this.__is_started = x

    def ret_isdead(this):
        return this.__isdead

    def upd_isdead(this, x):
        this.__isdead = x

    def ret_speed(this):
        return this.__speed

    def upd_speed(this, x):
        this.__speed = x

    def ret_damage(this):
        return this.__damage

    def upd_damage(this, x):
        this.__damage = x

    def ret_barbarian(this):
        return this.__barbarian
    
    def reset(this):
        this.upd_total_health(20)
        this.upd_health(20)
        this.upd_row(game_ht[1] - 1)
        this.upd_col(0)
        this.upd_isdead(0)
        this.upd_speed(1)
        this.upd_damage(10)
        
    def clear(this, screen):
        screen[this.ret_row()][this.ret_col()] = " "

    def show(this, screen):
        r = this.ret_row()
        c = this.ret_col()
        # if(this.ret_isdead()):
        #     screen[r][c] = " "
        screen[r][c] = this.ret_barbarian()
        
    