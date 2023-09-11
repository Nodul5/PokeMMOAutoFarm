# USING UTF-8

from pyautogui import *      
import time,random,functions,datetime, os

os.chdir("1.0")

click(1280,800) # Clique sur l'écran de gauche
PAUSE = 0
functions.goToPokeCenter()
while True:
    functions.fishingCycle()