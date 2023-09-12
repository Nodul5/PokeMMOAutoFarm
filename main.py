from pyautogui import *
from bin.constant import *
from bin.screenshot import *

import os, time, random, chat, pytesseract, farm

# TODO Etablir plusieurs fonctions goToPokecenter pour pouvoir choisir entre plusieurs spots de farm.

## Détecter la dernière ligne
chat = chat.Chat()
image1 = Screenshot()
imageChat = image1.getChat()

if(imageChat is not None):
    cv2.imshow("Chat",imageChat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(chat.imageToText(image1.getChat()))
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