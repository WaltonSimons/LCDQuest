import Globals
import DrawableObject

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps

import sys

# Raspberry Pi software SPI config:
SCLK = 17
DIN = 18
DC = 27
RST = 23
CS = 22

# Software SPI usage:
disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()

# Create image buffer.
screen = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

# Create drawing object.
draw = ImageDraw.Draw(screen)

# Draw a white filled box to clear the image.
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

# Set font.
font = ImageFont.truetype('LCDica.ttf', 17)


def draw_objects():
    draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
    Globals.drawdynamic.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=0, fill=0)
    for drawable in Globals.hierarchy:
        if sys.getrefcount(drawable) > 3:
            if drawable.visible:
                draw.bitmap((drawable.x, drawable.y), ImageOps.invert(drawable.image).convert('1'))
        else:
            del drawable
    for text in Globals.texts:
        if sys.getrefcount(text) > 3:
            if text.visible:
                draw.text((text.x, text.y), text.string, font=font)
        else:
            del text
    for dyn in Globals.dynamics:
        if sys.getrefcount(dyn) > 3:
            if dyn.visible:
                dyn.draw()
        else:
            del dyn


def refresh_screen():
    draw.bitmap((0, 0), Globals.dynamic)
    disp.image(screen)
    disp.display()


def clear_screen():
    disp.clear()
    disp.display()
