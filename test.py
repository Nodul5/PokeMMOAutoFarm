import pyautogui, functions

pyautogui.screenshot(imageFilename="screen du chat.png", region = functions.regionChat).show()
pyautogui.screenshot(imageFilename="screen des dialogues de pêche.png", region = functions.regionDialogue).show()