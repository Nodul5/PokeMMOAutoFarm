from pyautogui import *
from bin.constant import *
from PIL import ImageGrab

import os, pytesseract, time, win32gui

class Chat:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

        self.historiqueMessage = []
        self.hwnd = 0 # Entier qui permet d'identifier la fenetre avec win32gui
        self.position = (0,0)
        self.size = (0,0)

        self.getPokeMMOWindowInfo() # Met à jour le self.hwnd, position et size

        print(self.hwnd)
        win32gui.SetForegroundWindow(self.hwnd) # Met la fenetre au Premier plan
        time.sleep(1)
        self.screenshotPokeMMOWindow().show()
        


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
    
    def convertWindowTitleUnicodeCaractersIntoAscii(self, string):
        ## https://en.wikipedia.org/wiki/Cyrillic_script_in_Unicode
        ## Le nom du jeu change à chaque fois qu'il se relance, avec des caractères comme U+0420 qui ressemble a un P en Ascii mais n'en n'est pas un.
        string = string.replace(u"\u0420","P")
        string = string.replace(u"\u0435", "e")
        string = string.replace(u"\u041c","M")
        string = string.replace(u"\u041e", "O")
        return string

    def getWindowInfo(self, hwnd, extra):
        if(win32gui.GetWindowText(hwnd) != ""): print(f"Window Title : {win32gui.GetWindowText(hwnd)}")
        if(WINDOW_NAME == self.convertWindowTitleUnicodeCaractersIntoAscii(win32gui.GetWindowText(hwnd))): 
            self.hwnd = hwnd
            rect = win32gui.GetWindowRect(hwnd)
            x = rect[0]
            y = rect[1]
            w = rect[2] - x
            h = rect[3] - y
            self.position = (x, y)
            self.size = (w, h)

    def getPokeMMOWindowInfo(self): 
        win32gui.EnumWindows(self.getWindowInfo, None)
        if(self.hwnd == 0):
            raise RuntimeError("La fenêtre PokeMMO n'a pas été trouvée !")
        
    def screenshotPokeMMOWindow(self):
        self.dimensions = list(win32gui.GetWindowRect(self.hwnd))
        self.dimensions[0] += 8
        self.dimensions[3] -= 8
        return ImageGrab.grab(self.dimensions, all_screens=True)
        #return ImageGrab.grab(bbox=(-2000,-2000,5000,5000), all_screens=True)