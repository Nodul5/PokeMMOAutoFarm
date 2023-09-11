from pyautogui import *
from bin.constant import *

import os, pytesseract, time

class Chat:
    def __init__(self):
        self.historiqueMessage = []
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    def start(self):
        self.useTeamChatAsGuide()
        time.sleep(2)
        self.lastLineBox = self.locateLastLine()

    def write(self, text):
        press('enter')
        write(text, interval=0.1)
        press('enter')

    def teamWrite(self, text):
        self.write(f"/team {text}")

    def useTeamChatAsGuide(self):
        self.teamWrite(f"Yo c'est {os.getlogin()}")
        self.teamWrite(f"Je vais commencer")
        self.teamWrite(f"a farm l'argent")
        self.teamWrite(f"avec mon Miaouss Jackpot")

    def locateLastLine(self):
        #TODO Améliorer la détection de la dernière ligne
        return locateOnScreen(os.path.join("image","lastLine.png"), confidence = 0.8)

    def lastLineScreenshot(self):
        return screenshot(region=self.lastLineBox)

    def getLastLine(self) -> str:
        return pytesseract.pytesseract.image_to_string(self.lastLineScreenshot())