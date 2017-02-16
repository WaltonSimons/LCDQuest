from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps

import pygame
import time

import LCDDrawer
import DrawableObject
import UI
import Battle
import Enemies
import Title
import Controller
import Player
import sys

p1 = Player.Player(50, 20, 10, 10, 10, 10, 10, portrait_num=1)
battle = Battle.Battle(player=p1, enemy1=Enemies.Enemy('Medusa Head', 15, 5, 10, 10, 'medusa'), enemy2=Enemies.Enemy('Skeleton', 15, 5, 5, 10, 'skeleton'), enemy3=Enemies.Enemy('Skeleton', 15, 5, 5, 10, 'skeleton'))
#title = Title.Title()
p1.battle = battle

RUNNING = True

LCDDrawer.draw_objects()
LCDDrawer.refresh_screen()

while RUNNING:
    LCDDrawer.draw_objects()
    LCDDrawer.refresh_screen()
    battle.battle_input()

LCDDrawer.clear_screen()