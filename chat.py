from pyautogui import *
from bin.constant import *
from PIL import ImageGrab

import os, pytesseract, time, win32gui

class Chat:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        self.messageHistory = []

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