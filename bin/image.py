import cv2
import numpy as np

## CONSTANT
CHAT_PADDING = 33

# read image
img = cv2.imread('./image/test.png')
ht, wd = img.shape[:2]
print(img.shape)

img = img[int(ht/2):ht, 0:int(wd/2)]
cv2.imwrite('./image/crop.png',img)

## Couleur de fond : #222222
BlueMin = np.array([34, 34, 34],np.uint8)
BlueMax = np.array([34, 34, 34],np.uint8)
mask = cv2.inRange(img, BlueMin, BlueMax)
cv2.imwrite('./image/mask.png',mask)

## Récupérer l'image masquée
#masked = cv2.bitwise_and(img,img, mask=mask)
#img = img - masked

# invert
#img = 255 - img
    
# get largest external contour
contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
big_contour = max(contours, key=cv2.contourArea)

# get bounding box of largest contour
x,y,w,h = cv2.boundingRect(big_contour)

# save resulting image
cv2.imwrite('./image/result.png',img[y:y+h-CHAT_PADDING, x:x+w])