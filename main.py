from pyautogui import *
from bin.constant import *
from bin.screenshot import *

import os, time, random, chat, pytesseract, farm

# TODO Etablir plusieurs fonctions goToPokecenter pour pouvoir choisir entre plusieurs spots de farm.

## Détecter la dernière ligne
chat = chat.Chat()
image1 = Screenshot()
imageChat = image1.getChat()
boxes = image1.getChatLineBoxes()

#n_boxes = len(boxes['level'])
#for i in range(n_boxes):
#    if (boxes['text'][i] != ""):
#        (x, y, w, h) = (boxes['left'][i], boxes['top'][i], boxes['width'][i], boxes['height'][i])
#        print(x,y,w,h)

if(imageChat is not None):
    print(chat.imageToText(imageChat))
else:
    print("ERREUR : Chat introuvable")


## Combattre en fonction des coordonnées de la dernière ligne
#farm = farm.Farm(chat)

#if(FARM_METHOD == "money"):
#    farm.money()
#elif(FARM_METHOD == "xp"):
#    farm.xp()
#else:
#    raise RuntimeError("Erreur dans la constante FARM_METHOD : Soit c'est money soit c'est xp")