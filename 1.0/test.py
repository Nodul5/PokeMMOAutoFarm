import pyautogui, functions, pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


pyautogui.screenshot(imageFilename="screen du chat.png", region = functions.regionChat).show()
pyautogui.screenshot(imageFilename="screen des dialogues de pêche.png", region = functions.regionDialogue).show()
#léo est un enculé