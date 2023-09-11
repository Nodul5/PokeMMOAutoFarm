from pyautogui import *
from constant import *

import os, pytesseract, time

class Chat:
    def __init__(self):
        self.historiqueMessage = []
        self.lastLineBox = self.getCoordsLastLine()
        self.engine = pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    def write(self, text):
        press(KEY_ENTER)
        write(text, interval=0.1)
        press(KEY_ENTER)

    def teamWrite(self, text):
        self.write(f"/team {text}")

    def remplir(self):
        self.teamWrite(f"Yo c'est {os.getlogin()}")
        self.teamWrite(f"Je vais commencer")
        self.teamWrite(f"a farm l'argent")
        self.teamWrite(f"avec mon Miaouss Jackpot")

    def locateLastLine(self):
        return locateOnScreen(os.path.join("image","lastLine.png"), confidence = 0.8)

    def lastLineScreenshot(self):
        return screenshot(region=self.lastLineBox)

    def getCoordsLastLine(self):
        self.remplir()
        time.sleep(2)
        return self.locateLastLine()

    def getLastLine(self) -> str:
        return pytesseract.pytesseract.image_to_string(self.lastLineScreenshot())