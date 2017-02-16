import DrawableObject
import UI
import Enemies
import Controller
import LCDDrawer
import Globals
import Stats

from PIL import Image

ENEMY1POS = (34, 13)


class Battle(object):

    def __init__(self, player=None, enemy1=None, enemy2=None, enemy3=None):
        Globals.battle = self
        self.b1 = UI.Button(3, 33, None, True)
        self.b2 = UI.Button(3, 41, None, False)
        self.b3 = UI.Button(44, 33, None, False)
        self.b4 = UI.Button(44, 41, None, False)
        self.currentbutton = self.b1
        self.downbox = UI.Static(0, 31, 'bottombox')
        self.upbox = UI.Static(0, 0, 'upperbox')
        self.bars = UI.Static(0, 26, 'statusbars')
        self.uptext = DrawableObject.Text(2, 2, '')
        self.downtext1 = DrawableObject.Text(3, 33, '')
        self.downtext2 = DrawableObject.Text(3, 41, '')
        self.o1 = DrawableObject.Text(13, 33, 'attack')
        self.o2 = DrawableObject.Text(13, 41, 'skills')
        self.o3 = DrawableObject.Text(54, 33, 'items')
        self.o4 = DrawableObject.Text(54, 41, 'status')
        self.enemyarrow = UI.Static(40, 10, 'enemyarrow', False)
        self.hpbar = UI.PixelBar(2, 30, 20)
        self.mpbar = UI.PixelBar(62, 30, 20)
        self.player = player
        self.enemy1 = enemy1
        self.enemy2 = enemy2
        self.enemy3 = enemy3
        self._currenttarget = enemy1
        if self.enemy1 is not None:
            self.enemy1.x = 34
            self.enemy1.y = 13
        if self.enemy2 is not None:
            self.enemy2.x = 9
            self.enemy2.y = 13
        if self.enemy3 is not None:
            self.enemy3.x = 59
            self.enemy3.y = 13
        self.turnorder = []
        self.battleover = False
        self.c = Controller.Control()
        self.action = None
        self.orderqueue = [player, enemy1, enemy2, enemy3]
        self.orderqueue.sort(key=lambda x: x.current_dex(), reverse=True)

    def hide(self):
        self.b1.visible = False
        self.b2.visible = False
        self.b3.visible = False
        self.b4.visible = False
        self.o1.visible = False
        self.o2.visible = False
        self.o3.visible = False
        self.o4.visible = False
        self.downbox.visible = False
        self.upbox.visible = False
        self.bars.visible = False
        self.uptext.visible = False
        self.downtext1.visible = False
        self.downtext2.visible = False
        self.hpbar.visible = False
        self.mpbar.visible = False
        if self.enemy1 is not None:
            self.enemy1.visible = False
        if self.enemy2 is not None:
            self.enemy2.visible = False
        if self.enemy3 is not None:
            self.enemy3.visible = False

    def unhide(self):
        self.b1.visible = True
        self.b2.visible = True
        self.b3.visible = True
        self.b4.visible = True
        self.o1.visible = True
        self.o2.visible = True
        self.o3.visible = True
        self.o4.visible = True
        self.downbox.visible = True
        self.upbox.visible = True
        self.bars.visible = True
        self.uptext.visible = True
        self.downtext1.visible = True
        self.downtext2.visible = True
        self.hpbar.visible = True
        self.mpbar.visible = True
        if self.enemy1 is not None:
            self.enemy1.visible = True
        if self.enemy2 is not None:
            self.enemy2.visible = True
        if self.enemy3 is not None:
            self.enemy3.visible = True

    def hide_bottom_box(self):
        self.b1.visible = False
        self.b2.visible = False
        self.b3.visible = False
        self.b4.visible = False
        self.o1.visible = False
        self.o2.visible = False
        self.o3.visible = False
        self.o4.visible = False

    def unhide_bottom_box(self):
        self.b1.visible = True
        self.b2.visible = True
        self.b3.visible = True
        self.b4.visible = True
        self.o1.visible = True
        self.o2.visible = True
        self.o3.visible = True
        self.o4.visible = True

    def show_message(self, message):
        self.hide_bottom_box()
        split = False
        if len(message) > 32:
            msg1 = message[0:31]
            if not (message[17] == ' ' or message[16] == ' '):
                msg1 += '-'
            msg2 = message[31:len(message)]
            if msg2[0] == ' ':
                msg2 = msg2[1:len(msg2)]
            self.show_message(msg1)
            self.show_message(msg2)
            split = True
        if len(message) > 18:
            msg1 = message[0:17]
            if not (message[17] == ' ' or message[16] == ' '):
                msg1 += '-'
            msg2 = message[17:len(message)]
            if msg2[0] == ' ':
                msg2 = msg2[1:len(msg2)]
        else:
            msg1 = message
            msg2 = ''
        if not split:
            self.downtext1.string = msg1
            self.downtext2.string = msg2
            LCDDrawer.draw_objects()
            LCDDrawer.refresh_screen()
            self.c.wait_for_input()
            self.unhide_bottom_box()
            self.downtext1.string = ''
            self.downtext2.string = ''
        self.update_bars()

    @property
    def currenttarget(self):
        return self._currenttarget

    @currenttarget.setter
    def currenttarget(self, value):
        self._currenttarget = value
        if value is not None:
            self.uptext.string = value.name

    def change_current_target(self, e):
        self.currenttarget = e
        if e is None:
            self.battle_end()
        if e == self.enemy1:
            self.enemyarrow.x = 40
        if e == self.enemy2:
            self.enemyarrow.x = 15
        if e == self.enemy3:
            self.enemyarrow.x = 65

    def change_current_button(self, b):
        self.currentbutton.deactivate()
        self.currentbutton = b
        self.currentbutton.activate()

    def button_control(self):
        c = self.c
        if c.right_arrow():
            if self.currentbutton == self.b1:
                self.change_current_button(self.b3)
            if self.currentbutton == self.b2:
                self.change_current_button(self.b4)
        if c.down_arrow():
            if self.currentbutton == self.b1:
                self.change_current_button(self.b2)
            if self.currentbutton == self.b3:
                self.change_current_button(self.b4)
        if c.left_arrow():
            if self.currentbutton == self.b3:
                self.change_current_button(self.b1)
            if self.currentbutton == self.b4:
                self.change_current_button(self.b2)
        if c.up_arrow():
            if self.currentbutton == self.b2:
                self.change_current_button(self.b1)
            if self.currentbutton == self.b4:
                self.change_current_button(self.b3)
        if c.ESC_button():
            self.battleover = False

    def target_chooser(self):
        c = self.c
        self.enemyarrow.visible = True
        self.uptext.string = self.currenttarget.name
        if c.left_arrow():
            if self.currenttarget == self.enemy1 and self.enemy2 is not None:
                self.change_current_target(self.enemy2)
            if self.currenttarget == self.enemy3 and (self.enemy1 is not None or self.enemy2 is not None):
                if self.enemy1 is not None:
                    self.change_current_target(self.enemy1)
                else:
                    self.change_current_target(self.enemy2)
        if c.right_arrow():
            if self.currenttarget == self.enemy1 and self.enemy3 is not None:
                self.change_current_target(self.enemy3)
            if self.currenttarget == self.enemy2 and (self.enemy1 is not None or self.enemy3 is not None):
                if self.enemy1 is not None:
                    self.change_current_target(self.enemy1)
                else:
                    self.change_current_target(self.enemy3)
        if c.A_button():
            self.player.attack(self.currenttarget)
            self.action = self.button_control
            self.enemyarrow.visible = False
            self.end_current_turn()
        if c.B_button():
            self.action = self.button_control
            self.enemyarrow.visible = False

    def battle_input(self):
        self.action = self.button_control
        self.update_bars()
        while not self.battleover:
            LCDDrawer.draw_objects()
            LCDDrawer.refresh_screen()
            if self.orderqueue[0] == self.player:
                self.c.wait_for_input()
                if self.c.A_button() and self.b1.active and self.action != self.target_chooser:
                    self.action = self.target_chooser
                    self.c.clear_input()
                if self.c.A_button() and self.b4.active:
                    self.hide()
                    s = Stats.EquipView()
                    self.action = s.equip_control
                    del s
                self.action()
            else:
                self.orderqueue[0].take_turn()
                self.end_current_turn()

    def get_next_living_enemy(self):
        if self.enemy1 is not None:
            return self.enemy1
        if self.enemy2 is not None:
            return self.enemy2
        if self.enemy3 is not None:
            return self.enemy3
        return None

    def end_current_turn(self):
        self.orderqueue.append(self.orderqueue.pop(0))

    def battle_end(self):
        self.show_message(self.player.name + ' wins!')
        self.battleover = True

    def update_bars(self):
        self.hpbar.filled = (100*self.player.hp)/self.player.maxhp
        self.mpbar.filled = (100*self.player.mp)/self.player.maxmp