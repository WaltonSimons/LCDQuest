import Enemies
import UI
import Battle
import Globals

from PIL import Image
from random import randint

class Item(object):

    def __init__(self, imagename):
        self.image = Image.open('items/' + imagename + '.png')


class Wearable(Item):

    def __init__(self, imagename):
        super(Wearable, self).__init__(imagename)

