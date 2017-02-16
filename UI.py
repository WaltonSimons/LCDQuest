import DrawableObject
import Globals

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Button(DrawableObject.Drawable):

    def __init__(self, x, y, action=None, active=False, visible=True):
        if active:
            img = Image.open('UI/full.png')
        else:
            img = Image.open('UI/empty.png')
        super(Button, self).__init__(x, y, img, 'UI', visible)
        self.action = action
        self.active = active

    def activate(self):
        self.active = True
        self.image = Image.open('UI/full.png')

    def deactivate(self):
        self.active = False
        self.image = Image.open('UI/empty.png')


class Static(DrawableObject.Drawable):

    def __init__(self, x, y, name, visible=True):
        img = Image.open('UI/' + name + '.png')
        super(Static, self).__init__(x, y, img, 'UI', visible)


class PixelBar(DrawableObject.Dynamic):

    def __init__(self, x, y, maxlength, filled=100, visible=True):
        super(PixelBar, self).__init__(x, y, visible)
        self.maxlength = maxlength
        self._filled = filled

    @property
    def filled(self):
        return self._filled

    @filled.setter
    def filled(self, value):
        self._filled = value
        if value <= 0:
            self.visible = False
        else:
            self.visible = True

    def draw(self):
        Globals.drawdynamic.line((self.x, self.y, self.x - 1 + (self.maxlength * self.filled)/100, self.y), fill=255)


class Bar(DrawableObject.Dynamic):

    def __init__(self, x, y, maxlength, height, filled=100, visible=True):
        super(Bar, self).__init__(x, y, visible)
        self.maxlength = maxlength
        self.height = height
        self._filled = filled

    @property
    def filled(self):
        return self._filled

    @filled.setter
    def filled(self, value):
        self._filled = value
        if value <= 0:
            self.visible = False
        else:
            self.visible = True

    def draw(self):
        Globals.drawdynamic.rectangle((self.x, self.y, self.x - 1 + (self.maxlength * self.filled)/100, self.y - 1 + self.height), fill=255)