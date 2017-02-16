import Adafruit_Nokia_LCD as LCD
from PIL import Image
from PIL import ImageDraw


hierarchy = []
texts = []
dynamics = []
battle = None
player = None
dynamic = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
drawdynamic = ImageDraw.Draw(dynamic)
drawdynamic.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=0, fill=0)
# drawdynamic.rectangle((10,10,20,20), outline=0, fill=0)
# drawdynamic.line((10, 10, 20, 50), fill=255)