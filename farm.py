from pyautogui import *
from bin.constant import *
from chat import *

import time, random

class Farm:
    def __init__(self, chat: Chat) -> None:
        self.earnings = []
        self.cash = 0
        self.chat = chat
        self.inFight = False
        self.dead = False

    def money(self, farmSpot: str) -> None:
        """
        Input: farmSport -> str, nom du fichier csv
        Output:\n None
        """
        #self.goHealAndGoBack(farmSpot)
        while True:
            if(self.inFight):
                lastLine = self.chat.getLastLine()
                if("est envoyé par" in lastLine or "vite l" in lastLine or "sauvage utilise" in lastLine):
                    self.wait(3)
                    self.csvInterpreter("jackpot")
                    print("test")
                elif(f"Restes de " in lastLine):
                    self.wait(3)
                    self.csvInterpreter("jackpot")
                    print("test")
                elif("plus de PP" in lastLine or (FIRST_POKEMON_NAME in lastLine and "K.O" in lastLine)):
                    self.inFight = False
                    self.goHealAndGoBack(farmSpot, FIRST_POKEMON_NAME in lastLine and "K.O" in lastLine)
                elif("$" in lastLine or "sac" in lastLine):
                    self.inFight = False
            else:
                self.fishingUntilGettingAFish()
                

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
            self.csvInterpreter('pokecenter')
            #self.goToPokecenter1()
            #self.csvInterpreter('pokecenter')
            #time.sleep(4)
            # Etape 3
            self.csvInterpreter('flocombe-xp-go')
            time.sleep(2)
            # Etape 4
            self.csvInterpreter('farm-xp-douxParfum')


            '''
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
                self.csvInterpreter('pokecenter')
                #self.goToPokecenter1(FIRST_POKEMON_NAME in lastLine and "K.O" in lastLine) 
            else:
                self.teleport()
            '''

    def goHealAndGoBack(self, farmSpot: str,dead=False) -> None:
        """
        Input : farmSpot -> str, dead -> bool (si besoin de switch de pokemon et de fuire ou non)
        Output : None\n
        Fuit le combat, en switchant de pokemon si nécessaire, puis retourne au spot de farm
        """
        if dead:
            self.switchToSecondPokemon()
        self.runAway()
        self.teleport()
        self.csvInterpreter("pokecenter-teleport")
        self.csvInterpreter(farmSpot)

    def wait(self,index=1):
        time.sleep(random.uniform(index-0.5,index+0.5))

    def switchToSecondPokemon(self):
        press(RIGHT)
        self.wait(1)
        press(KEY_VALID)
        self.wait(7)

    def keyUpkeyDown(self,key):
        keyDown(key)
        self.wait(0.5)
        keyUp(key)
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

    def teleport(self):
        press(KEY_TELEPORT)
        self.wait(5)

    def runAway(self):
        press(KEY_DOWN)
        self.wait()
        press(KEY_RIGHT)
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
            print(self.chat.getLastLine())
            if("sauvage" in self.chat.getLastLine() or "est envoy" in self.chat.getLastLine()):
                self.inFight = True
                return 0
            
    def csvInterpreter(self,filename):
        filepath = "./src/" + filename + ".csv"
        with open(filepath) as file:
            lines = file.readlines()
            for l in lines:
                print(l)
                cels = l.split(";")
                if(cels[0] == "keyUpkeyDownDelayed"):
                    k = cels[1]
                    t = float(cels[2]) if('.' in cels[2]) else int(cels[2])
                    self.keyUpkeyDownDelayed(CONSTANTS[k],t)
                elif(cels[0] == "keyUpkeyDown"):
                    k = cels[1].replace("\n","")
                    self.keyUpkeyDown(CONSTANTS[k])
                elif(cels[0] == "keyUp"):
                    k = cels[1].replace("\n","")
                    keyUp(CONSTANTS[k])
                elif(cels[0] == "keyDown"):
                    k = cels[1].replace("\n","")
                    keyDown(CONSTANTS[k])
                elif(cels[0] == "wait"):
                    t = cels[1].replace("\n","")
                    t = float(t) if('.' in t) else int(t)
                    time.sleep(t)
                elif(cels[0] == "press"):
                    k = cels[1]
                    press(k)
                else:
                    print("ERREUR lors de l'interprétation de la ligne suivante en csv : ",l)