from pyautogui import *

def screenshotDialogue(name):
    fishingDialogue = screenshot(region=(550,140,700,120)).save(name)