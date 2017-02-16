import LCDDrawer
import Battle
import Globals
import DrawableObject
from PIL import Image
from random import randint


class Enemy(DrawableObject.Drawable):

    def __init__(self, name, maxhp, attack, xp, dex, imagename):
        super(Enemy, self).__init__(100, 100, Image.open('enemies/' + imagename + '.png'), 'Enemies')
        self.name = name
        self.maxhp = maxhp
        self._hp = maxhp
        self.attack = attack
        self.xp = xp
        self.dex = dex

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if value > 0:
            self._hp = value
        else:
            self._hp = 0
            self.die()

    def current_dex(self):
        return self.dex

    def take_turn(self):
        self.attack_move(Globals.battle.player)

    def attack_move(self, target):
        damage = self.attack + randint(-self.attack/6, self.attack/6)
        Globals.battle.show_message(self.name + ' attacks!')
        Globals.battle.show_message(self.name + ' hits ' + Globals.battle.player.name + ' for ' + str(damage) + ' damage!')
        Globals.battle.player.hp -= damage

    def die(self):
        print 'kupa'
        Globals.battle.show_message(self.name + ' dies!')
        Globals.battle.show_message(Globals.player.name + ' gained ' + str(self.xp) + ' XP!')
        if Globals.battle.enemy1 == self:
            Globals.battle.enemy1 = None
        if Globals.battle.enemy2 == self:
            Globals.battle.enemy2 = None
        if Globals.battle.enemy3 == self:
            Globals.battle.enemy3 = None
        Globals.hierarchy.remove(self)
        Globals.battle.orderqueue.remove(self)
        Globals.battle.change_current_target(Globals.battle.get_next_living_enemy())
