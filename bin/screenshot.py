from bin.constant import *
from PIL import ImageGrab, Image
import cv2
import numpy as np
import win32gui, time
import pytesseract

## CONSTANT
CHAT_PADDING = 33

class Screenshot:
    def __init__(self):
        self.hwnd = 0 # Entier qui permet d'identifier la fenetre avec win32gui
        self.screenshot = None
        self.cropped = None

    def getChat(self):
        self.screenshot = self.screenshotPokeMMOWindow()
        return self.cropChat()
    
    def getChatLineBoxes(self):
        self.screenshot = self.screenshotPokeMMOWindow()
        return pytesseract.image_to_boxes(self.screenshot, output_type=pytesseract.Output.DICT)

    def cropChat(self):
        # On prend le quart bas gauche du screen
        ht, wd = self.screenshot.shape[:2]
        self.screenshot = self.screenshot[int(ht/2):ht, 0:int(wd/2)]

        ## Mask en fonction de la couleur de fond du chat : #222222
        BlueMin = np.array([33, 33, 33],np.uint8)
        BlueMax = np.array([35, 35, 35],np.uint8)
        mask = cv2.inRange(self.screenshot, BlueMin, BlueMax)
            
        # Récupération du contour du chat
        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]
        if(len(contours) > 0):
            big_contour = max(contours, key=cv2.contourArea)
            x,y,w,h = cv2.boundingRect(big_contour)

            self.cropped = self.screenshot[y:y+h-CHAT_PADDING, x:x+w]
            return self.cropped
        else:
            return None
    
    def convertWindowTitleUnicodeCaractersIntoAscii(self, string):
            ## https://en.wikipedia.org/wiki/Cyrillic_script_in_Unicode
            ## Le nom du jeu change à chaque fois qu'il se relance, avec des caractères comme U+0420 qui ressemble a un P en Ascii mais n'en n'est pas un.
            string = string.replace(u"\u0420","P")
            string = string.replace(u"\u0435", "e")
            string = string.replace(u"\u041c","M")
            string = string.replace(u"\u041e", "O")
            return string

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

    def getPokeMMOWindowInfo(self): 
        win32gui.EnumWindows(self.getWindowInfo, None)
        if(self.hwnd == 0):
            raise RuntimeError("La fenêtre PokeMMO n'a pas été trouvée !")
        
    def screenshotPokeMMOWindow(self):
        #self.getFocus()
        self.getPokeMMOWindowInfo() # Met à jour le self.hwnd, position et size
        self.dimensions = list(win32gui.GetWindowRect(self.hwnd))
        self.dimensions[0] += 8
        self.dimensions[1] += 8
        screen = ImageGrab.grab(self.dimensions, all_screens=True)
        return np.asarray(screen)[:, :, ::-1]
    
    def getLastLine(self):
        if(self.cropped is None):
            self.getChat()

        h,w = np.shape(self.cropped)[0:2]
        #cv2.imshow('result',self.cropped[h-26:h, 0:w])
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        return self.cropped[h-26:h, 0:w]

    def getFocus(self):
        self.getPokeMMOWindowInfo() # Met à jour le self.hwnd, position et size
        win32gui.SetForegroundWindow(self.hwnd) # Met la fenetre au premier plan
        time.sleep(1)