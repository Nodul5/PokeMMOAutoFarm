from pyautogui import *
from bin.constant import *

import time, random

class Farm:
    def __init__(self, chat) -> None:
        self.recompenses = []
        self.money = 0
        self.chat = chat
        self.dead = False

    def money(self):
        while True:
            lastLine = self.chat.getLastLine()
            self.fishingUntilGettingAFish()
            if(f"{FIRST_POKEMON_NAME} est envoyé par" in lastLine):
                self.wait(3)
                self.jackpot()
            elif(f"Restes de {FIRST_POKEMON_NAME}" in lastLine):
                self.wait(3)
                self.jackpot()
            elif("plus de PP" in lastLine or (FIRST_POKEMON_NAME in lastLine and "K.O" in lastLine)):
                self.wait(3)
                self.runAway()
                self.wait(5)
                self.goToPokecenter(FIRST_POKEMON_NAME in lastLine and "K.O" in lastLine)
    
    def xp(self):
        while True:
            lastLine = self.chat.getLastLine()
            self.fishingUntilGettingAFish()
            if(f"{FIRST_POKEMON_NAME} est envoyé par" in lastLine):
                self.wait(3)
                self.jackpot()
            elif(f"Restes de {FIRST_POKEMON_NAME}" in lastLine):
                self.wait(3)
                self.jackpot()
            elif("plus de PP" in lastLine or (FIRST_POKEMON_NAME in lastLine and "K.O" in lastLine)):
                self.wait(3)
                self.runAway()
                self.wait(5)
                self.goToPokecenter(FIRST_POKEMON_NAME in lastLine and "K.O" in lastLine)

    def wait(self,index=1):
        time.sleep(random.uniform(index-0.5,index+0.5))

    def switchToSecondPokemon(self):
        press(RIGHT)
        self.wait(1)
        press(KEY_VALID)

    def goToPokecenter(self, dead):
        if dead:
            self.switchToSecondPokemon()
        self.wait(7)
        press(KEY_DOWN)
        self.wait(2)
        press(KEY_RIGHT)
        self.wait(2)
        press(KEY_VALID)
        self.wait(6)
        self.teleport()
        self.wait(7)
        keyUp(KEY_VALID)
        self.wait(1)
        keyDown(KEY_VALID)
        self.wait(2)
        press(KEY_VALID)
        self.wait(2)
        press(KEY_VALID)
        self.wait(7)
        press(KEY_VALID)
        self.wait(2)
        press(KEY_VALID)
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
        press(KEY_VALID)
    
    def jackpot(self):
        press(KEY_VALID)
        self.wait()
        press(KEY_VALID)

    def larcin(self):
        press(KEY_VALID)
        self.wait()
        press(KEY_RIGHT)
        self.wait()
        press(KEY_VALID)

    def fishingUntilGettingAFish(self):
        while True:
            press(KEY_FISHING)
            time.sleep(random.uniform(4.0,4.25))
            press(KEY_VALID)
            if("sauvage" in self.chat.getLastLine()):
                return 0