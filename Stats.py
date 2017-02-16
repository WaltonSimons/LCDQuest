import DrawableObject
import UI
import Controller
import LCDDrawer
import Globals

from PIL import Image

class StatsView(object):

    def __init__(self):
        self.statusbox = UI.Static(0, 0, 'statusbox')
        self.portraitframe = UI.Static(61, 11, 'portraitframe')
        self.portrait = DrawableObject.Drawable(63, 13, Globals.player.portrait)
        self.nametext = DrawableObject.Text(2, 2, Globals.player.name)
        self.leveltext = DrawableObject.Text(65, 2, 'LV.' + "%02d"%Globals.player.level)
        self.strtext = DrawableObject.Text(3, 11, 'STR')
        self.deftext = DrawableObject.Text(33, 11, 'DEF')
        self.inttext = DrawableObject.Text(3, 17, 'INT')
        self.somtext = DrawableObject.Text(3, 11, 'STR')
        self.dextext = DrawableObject.Text(3, 23, 'DEX')
        self.lcktext = DrawableObject.Text(33, 23, 'LCK')
        self.strnum = DrawableObject.Text(20, 11, "%02d"%Globals.player.stren)
        self.defnum = DrawableObject.Text(50, 11, "%02d"%Globals.player.defen)
        self.intnum = DrawableObject.Text(20, 17, "%02d"%Globals.player.inte)
        self.somnum = DrawableObject.Text(20, 11, "%02d"%Globals.player.stren)
        self.dexnum = DrawableObject.Text(20, 23, "%02d"%Globals.player.dex)
        self.lcknum = DrawableObject.Text(50, 23, "%02d"%Globals.player.lck)
        self.hptext = DrawableObject.Text(3, 33, 'HP')
        self.mptext = DrawableObject.Text(3, 40, 'MP')
        self.bars = UI.Static(14, 33, 'statusviewbars')
        self.hpnumber = DrawableObject.Text(55, 33, "%03d"%Globals.player.hp + '/' + "%03d"%Globals.player.maxhp)
        self.mpnumber = DrawableObject.Text(55, 40, "%03d"%Globals.player.mp + '/' + "%03d"%Globals.player.maxmp)
        self.hpbar = UI.Bar(15, 34, 37, 3, (100*Globals.player.hp)/Globals.player.maxhp)
        self.mpbar = UI.Bar(15, 41, 37, 3, (100*Globals.player.mp)/Globals.player.maxmp)

    def stats_control(self):
        if Globals.battle.c.B_button():
            Globals.battle.action = Globals.battle.button_control
            Globals.battle.unhide()
        if Globals.battle.c.right_arrow():
            e = EquipView()
            Globals.battle.action = e.equip_control


class EquipView(object):

    def __init__(self):
        self.equipbox = UI.Static(0, 0, 'equipbox')
        self.headtext = DrawableObject.Text(2, 2, 'head')
        self.armortext = DrawableObject.Text(2, 8, 'armor')
        self.handstext = DrawableObject.Text(2, 14, 'hands')
        self.weapontext = DrawableObject.Text(2, 20, 'weapon')
        self.headname = DrawableObject.Text(35, 2, '-')
        self.armorname = DrawableObject.Text(35, 8, '-')
        self.handsname = DrawableObject.Text(35, 14, '-')
        self.weaponname = DrawableObject.Text(35, 20, '-')
        self.arrow = UI.Static(30, 2, 'equiparrow')
        self.upchoice = Globals.player.head
        self.down1text = DrawableObject.Text(3, 29, '')
        self.down2text = DrawableObject.Text(3, 35, '')
        self.down3text = DrawableObject.Text(3, 35, '')

    def equip_control(self):
        if Globals.battle.c.B_button():
            Globals.battle.action = Globals.battle.button_control
            Globals.battle.unhide()
        if Globals.battle.c.left_arrow():
            e = StatsView()
            Globals.battle.action = e.stats_control