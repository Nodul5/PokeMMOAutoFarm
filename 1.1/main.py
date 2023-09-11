from pyautogui import *
from constant import *
import os, time, random, chat, pytesseract, fight

os.chdir("1.1")

chat = chat.Chat()
fight = fight.Fight(chat)