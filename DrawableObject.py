import Globals


class Drawable(object):

    def __init__(self, x, y, image, group='', visible=True):
        self.x = x
        self.y = y
        self.image = image
        self.group = group
        self.visible = visible
        Globals.hierarchy.append(self)


class Text(object):

    def __init__(self, x, y, string='', visible=True):
        self.x = x
        self.y = y - 5
        self.string = string
        self.visible = visible
        Globals.texts.append(self)


class Dynamic(object):

    def __init__(self, x, y, visible=True):
        self.x = x
        self.y = y
        self.visible = visible
        Globals.dynamics.append(self)

    def draw(self):
        pass
