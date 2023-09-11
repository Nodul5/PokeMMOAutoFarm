from pyautogui import *
from constant import *

import time, random

class Fight:
    def __init__(self, chat) -> None:
        self.recompenses = []
        self.money = 0
        self.chat = chat
        self.dead = False

        while True:
            lastLine = chat.getLastLine()
            self.fishingUntilGettingAFish()
            if(f"{MIAOUSS_NAME} est envoyé par" in lastLine):
                self.wait(3)
                self.jackpot()
            elif(f"Restes de {MIAOUSS_NAME}" in lastLine):
                self.wait(3)
                self.jackpot()
            elif("plus de PP" in lastLine or (MIAOUSS_NAME in lastLine and "K.O" in lastLine)):
                self.wait(3)
                self.runAway()
                self.wait(5)
                self.goToPokecenter(MIAOUSS_NAME in lastLine and "K.O" in lastLine)
    
    def wait(self,index=1):
        time.sleep(random.uniform(index-0.5,index+0.5))

    def switchToSecondPokemon(self):
        press(RIGHT)
        self.wait(1)
        press(KEY_ENTER)

    def goToPokecenter(self, dead):
        if dead:
            self.switchToSecondPokemon()
        self.wait(7)
        press(KEY_DOWN)
        self.wait(2)
        press(KEY_RIGHT)
        self.wait(2)
        press(KEY_ENTER)
        self.wait(6)
        self.teleport()
        self.wait(7)
        keyUp(KEY_ENTER)
        self.wait(1)
        keyDown(KEY_ENTER)
        self.wait(2)
        press(KEY_ENTER)
        self.wait(2)
        press(KEY_ENTER)
        self.wait(7)
        press(KEY_ENTER)
        self.wait(2)
        press(KEY_ENTER)
        self.wait(2)
        keyDown(KEY_CANCEL)
        keyDown(KEY_DOWN)
        self.wait(4)
        keyUp(KEY_DOWN)
        keyDown(KEY_LEFT)
        self.wait(2)
        keyUp(LEFT)
        keyDown(KEY_DOWN)
        self.wait(2)
        keyUp(KEY_DOWN)
        keyUp(KEY_CANCEL)

    def teleport(self):
        press(KEY_TELEPORT)

    def runAway(self):
        press(KEY_DOWN)
        self.wait()
        press(KEY_RIGHT)
        self.wait()
        press(KEY_ENTER)
    
    def jackpot(self):
        press(KEY_ENTER)
        self.wait()
        press(KEY_ENTER)

    def larcin(self):
        press(KEY_ENTER)
        self.wait()
        press(KEY_RIGHT)
        self.wait()
        press(KEY_ENTER)

    def fishingUntilGettingAFish(self):
        while True:
            press(KEY_FISHING)
            time.sleep(random.uniform(4.0,4.25))
            press(KEY_ENTER)
            if("sauvage" in self.chat.getLastLine()):
                return 0