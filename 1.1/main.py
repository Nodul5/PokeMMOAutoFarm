from pyautogui import *
from constant import *
import os, time, random, chat, pytesseract, fight

os.chdir("1.1")

past = time.time()
print(past)
click(1280,800)
now = time.time()
print(now - past)

# Détecter la dernière ligne
chat = chat.Chat()

# Combattre en fonction des coordonnées de la dernière ligneo
fight = fight.Fight(chat)