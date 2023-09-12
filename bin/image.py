import cv2
import numpy as np

## CONSTANT
CHAT_PADDING = 33

class Image:
    def __init__(self,image):
        self.image = image
    
    def cropChat(self):
        # On prend le quart bas gauche du screen
        ht, wd = self.image.shape[:2]
        self.image = self.image[int(ht/2):ht, 0:int(wd/2)]

        ## Mask en fonction de la couleur de fond du chat : #222222
        BlueMin = np.array([34, 34, 34],np.uint8)
        BlueMax = np.array([34, 34, 34],np.uint8)
        mask = cv2.inRange(self.image, BlueMin, BlueMax)
            
        # Récupération du contour du chat
        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]
        big_contour = max(contours, key=cv2.contourArea)
        x,y,w,h = cv2.boundingRect(big_contour)

        self.cropped = self.image[y:y+h-CHAT_PADDING, x:x+w]
        return self.cropped