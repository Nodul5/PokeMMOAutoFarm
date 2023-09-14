from pyautogui import *
from bin.constant import *
from bin.screenshot import *
from PIL import ImageGrab

import os, pytesseract, time, win32gui

class Chat:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        self.messageHistory = []
        self.getFocus()
        #self.start()

    def start(self):
        for i in range(0,10):
            self.teamWrite("test")

    def write(self, text):
        press('enter')
        write(text, interval=0.1)
        press('enter')

    def teamWrite(self, text):
        self.write(f"/team {text}")

    def imageToText(self, image) -> str:
        return pytesseract.image_to_string(image)
    
    def saveInHistory(self, text):
        self.messageHistory.append(text)

    def checkIfInHistory(self, text):
        return text in self.messageHistory
    
    def getPokeMMOWindowInfo(self): 
        win32gui.EnumWindows(self.getWindowInfo, None)
        if(self.hwnd == 0):
            raise RuntimeError("La fenêtre PokeMMO n'a pas été trouvée !")
        
    def getLastLine(self):
        image1 = Screenshot()
        imageLastLine = image1.getLastLine()
        return imageLastLine
        
    def getFocus(self):
        self.getPokeMMOWindowInfo() # Met à jour le self.hwnd, position et size
        win32gui.SetForegroundWindow(self.hwnd) # Met la fenetre au premier plan
        time.sleep(1)

    def getWindowInfo(self, hwnd, extra):
        #if(win32gui.GetWindowText(hwnd) != ""): print(f"Window Title : {win32gui.GetWindowText(hwnd)}")
        if(WINDOW_NAME == self.convertWindowTitleUnicodeCaractersIntoAscii(win32gui.GetWindowText(hwnd))): 
            self.hwnd = hwnd
            rect = win32gui.GetWindowRect(hwnd)
            x = rect[0]
            y = rect[1]
            w = rect[2] - x
            h = rect[3] - y
            self.position = (x, y)
            self.size = (w, h)

    def convertWindowTitleUnicodeCaractersIntoAscii(self, string):
        ## https://en.wikipedia.org/wiki/Cyrillic_script_in_Unicode
        ## Le nom du jeu change à chaque fois qu'il se relance, avec des caractères comme U+0420 qui ressemble a un P en Ascii mais n'en n'est pas un.
        string = string.replace(u"\u0420","P")
        string = string.replace(u"\u0435", "e")
        string = string.replace(u"\u041c","M")
        string = string.replace(u"\u041e", "O")
        return string