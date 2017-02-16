import DrawableObject
import UI
import Controller
import LCDDrawer
import Globals

class PortraitScreen():

    def __init__(self):
        self.frame = UI.Static(0, 0, 'gameframe')
        self.uppertext = DrawableObject.Text(9, 2, 'Choose a portrait')
        self.portraitframe = UI.Static(32, 14, 'portraitframe')
