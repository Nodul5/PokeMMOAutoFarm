from pyautogui import *
from bin.constant import *
from bin.screenshot import *
from chat import *

import os, time, random, pytesseract, farm

# TODO Etablir plusieurs fonctions goToPokecenter pour pouvoir choisir entre plusieurs spots de farm.

click(1200,800)

## Détecter la dernière ligne
chat = Chat()

print(chat.getLastLine())
click(1200,800)
time.sleep(random.uniform(1-0.5,1+0.5))


## Combattre en fonction des coordonnées de la dernière ligne
farm = farm.Farm(chat)

if(FARM_METHOD == "money"):
    farm.money()
elif(FARM_METHOD == "xp"):
    farm.xp()
else:
    raise RuntimeError("Erreur dans la constante FARM_METHOD : Soit c'est money soit c'est xp")
