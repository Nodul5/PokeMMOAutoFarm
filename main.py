from pyautogui import *
from bin.constant import *
from bin.screenshot import *

import os, time, random, chat, pytesseract, farm

# TODO Etablir plusieurs fonctions goToPokecenter pour pouvoir choisir entre plusieurs spots de farm.

## Détecter la dernière ligne
chat = chat.Chat()
#image1 = Screenshot()
#imageLastLine = image1.getLastLine()
imageLastLine = chat.getLastLine()

if(imageLastLine is not None):
    print(chat.imageToText(imageLastLine))
else:
    print("ERREUR : Chat introuvable")

click(1200,800)
time.sleep(random.uniform(1-0.5,1+0.5))
write(['space'])


## Combattre en fonction des coordonnées de la dernière ligne
'''
farm = farm.Farm(chat)

if(FARM_METHOD == "money"):
    farm.money()
elif(FARM_METHOD == "xp"):
    farm.xp()
else:
    raise RuntimeError("Erreur dans la constante FARM_METHOD : Soit c'est money soit c'est xp")
'''