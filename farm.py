from pyautogui import *
from bin.constant import *

import time, random

class Farm:
    def __init__(self, chat) -> None:
        self.earnings = []
        self.cash = 0
        self.chat = chat
        self.dead = False

    def money(self):
        self.teleport()
        self.goToPokecenter2()
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
                self.goToPokecenter2(FIRST_POKEMON_NAME in lastLine and "K.O" in lastLine)
    
    def xp(self):
        # TODO 
        # Etape 1 - Vol à Flocombe
        # Etape 2 - Entrer dans le pokécentre puis se soigner
        # Etape 3 - Aller dans la zone surf de la tour dracospire
        # Etape 4 - Se placer sur l'eau et doux parfum
        # Etape 5 - Se battre
        # Etape 6 - Recommencer à l'étape 2 à l'infini
        # Etape 7 - Se soigner quand plus de PP ou mort

        while True:
            # Etape 1
            #self.flyTo('Flocombe')
            self.csvInterpreter('flocombe-flyTo')

            # Etape 2
            self.csvInterpreter('flocombe-pokecenter')
            #self.goToPokecenter1()
            lastLine = self.chat.getLastLine()
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
                self.goToPokecenter1(FIRST_POKEMON_NAME in lastLine and "K.O" in lastLine)
            else:
                self.teleport()

    def wait(self,index=1):
        time.sleep(random.uniform(index-0.5,index+0.5))

    def switchToSecondPokemon(self):
        press(RIGHT)
        self.wait(1)
        press(KEY_VALID)

    def keyUpkeyDown(self,key):
        keyDown(key)
        print("press",key)
        self.wait(0.5)
        keyUp(key)
        print("release",key)
        self.wait(0.5)

    def keyUpkeyDownDelayed(self,key,t):
        keyDown(key)
        time.sleep(t)
        keyUp(key)

    def flyTo(self,city):
        if(city == "Flocombe"):
            keyDown(KEY_VOL)
            time.sleep(0.1)
            keyUp(KEY_VOL)

            keyDown('z')
            time.sleep(5)
            keyUp('z')
            keyDown('q')
            time.sleep(5)
            keyUp('q')

            keyDown('d')
            time.sleep(0.65)
            keyUp('d')
            keyDown('s')
            time.sleep(0.5)
            keyUp('s')

            self.keyUpkeyDown(KEY_VALID)

    def goToPokecenter1(self):
        print("Entrer dans le pokécenter")
        keyDown('z')
        time.sleep(7)
        keyUp('z')
        keyDown(KEY_VALID)
        time.sleep(8)
        keyUp(KEY_VALID)
        keyDown('s')
        time.sleep(4)
        keyUp('s')

        '''
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
        '''

    def goToPokecenter2(self, dead=False):
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
        self.wait(5)

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
            
    def csvInterpreter(self,filepath):
        filepath = "./src/" + filepath + ".csv"
        with open(filepath) as file:
            lines = file.readlines()
            for l in lines:
                cels = l.split(";")
                if(cels[0] == "keyUpkeyDownDelayed"):
                    k = cels[1]
                    t = float(cels[2]) if('.' in cels[2]) else int(cels[2])
                    self.keyUpkeyDownDelayed(CONSTANTS[k],t)
                elif(cels[0] == "keyUpkeyDown"):
                    k = cels[1]
                    self.keyUpkeyDown(CONSTANTS[k])
                else:
                    print("ERREUR lors de l'interprétation de la ligne suivante en csv : ",l)