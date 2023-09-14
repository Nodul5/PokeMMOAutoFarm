from pyautogui import *
from bin.constant import *
from bin.screenshot import *

import os, time, random, chat, pytesseract, farm

# TODO Etablir plusieurs fonctions goToPokecenter pour pouvoir choisir entre plusieurs spots de farm.

## Détecter la dernière ligne
image1 = Screenshot()
imageLastLine = image1.getLastLine()
chat = chat.Chat()

if(imageLastLine is not None):
    print(chat.imageToText(imageLastLine))
else:
    print("ERREUR : Chat introuvable")


## Combattre en fonction des coordonnées de la dernière ligne
#farm = farm.Farm(chat)

if(FARM_METHOD == "money"):
    farm.money()
elif(FARM_METHOD == "xp"):
    farm.xp()
else:
    raise RuntimeError("Erreur dans la constante FARM_METHOD : Soit c'est money soit c'est xp")