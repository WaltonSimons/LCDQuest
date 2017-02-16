import Enemies
import UI
import Battle
import Globals

from PIL import Image
from random import randint

class Player:

    def __init__(self, maxhp, maxmp, stren, inte, dex, defen, lck, name='Bob', job = '', portrait_num = 1, level = 1):
        Globals.player = self
        self.maxhp = maxhp
        self.hp = maxhp
        self.maxmp = maxmp
        self.mp = maxmp
        self.stren = stren
        self.inte = inte
        self.dex = dex
        self.defen = defen
        self.lck = lck
        self.name = name
        self.job = job
        self.portrait = Image.open('portraits/' + str(portrait_num) + '.png')
        self.level = level
        self.head = None
        self.armor = None
        self.hands = None
        self.weapon = None

    def attack(self, enemy):
        damage = self.stren + randint(-self.stren/6, self.stren/6)
        Globals.battle.show_message(self.name + ' hits ' + enemy.name + ' for ' + str(damage) + ' damage!')
        enemy.hp = enemy.hp - damage

    def current_dex(self):
        return self.dex
