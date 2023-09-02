# USING UTF-8

from pyautogui import *
import pytesseract, pyautogui, datetime, time, random, tkinter

tk = tkinter.Tk()
regionChat = (5,1140,395,20)
regionDialogue = (550,140,700,120)
screenResolution = [tk.winfo_screenwidth(),tk.winfo_screenheight()]
screenCenter = [screenResolution[0]//2, screenResolution[1]//2]
bindAbra = "9"

print(screenCenter)

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def pressFishingKey():
    press('"')

def isOnScreen(image):
    positions = locateOnScreen(image, confidence=1)
    print(positions)
    return positions != None  

def goToPokeCenter(dead = False):
    if dead:
        click(614,805) #Switch sur deuxieme pokemon
    time.sleep(round(random.uniform(6.5, 6.75), 2))
    press("s")
    time.sleep(round(random.uniform(1.5, 1.75), 2))
    press("d")
    time.sleep(round(random.uniform(1.5, 1.75), 2))
    press("space")
    time.sleep(round(random.uniform(5.5, 5.75), 2))
    press(bindAbra)
    time.sleep(round(random.uniform(6, 6.5), 2))
    log("Retour au centre pokémon.")
    keyUp("space")
    time.sleep(0.5)
    keyDown("space")
    time.sleep(round(random.uniform(1.5, 1.75), 2))
    press("space")
    time.sleep(round(random.uniform(1.5, 1.75), 2))
    press("space")
    time.sleep(round(random.uniform(7.5, 7.75), 2))
    press("space")
    time.sleep(round(random.uniform(1.5, 1.75), 2))
    press("space")
    time.sleep(round(random.uniform(1.5, 1.75), 2))
    keyDown("s")
    time.sleep(5)
    keyUp("s")
    keyDown("q")
    time.sleep(1.5)
    keyUp("q")
    keyDown("s")
    time.sleep(3)
    keyUp("s")

def restorePP():
    time.sleep(round(random.uniform(4, 4.5), 2))
    click(600,860) #clique sur fuite          
    time.sleep(round(random.uniform(1.5, 1.75), 2))
    press("b")                                             #ouvre le sac
    time.sleep(round(random.uniform(2.5, 2.75), 2))
    hotkey("ctrl","f")                                     #met le focus dans la barre de recherche
    time.sleep(round(random.uniform(1.5, 1.75), 2))
    write("baie mepo",interval=0.5)                        #tappe "baie mepo"
    time.sleep(round(random.uniform(1.5, 1.75), 2))
    click(1416,914)                                        #clique sur la baie mepo (mettre le sac en bas a droite)
    #click(locateCenterOnScreen("baieMepo.png"))
    time.sleep(round(random.uniform(1.5, 1.75), 2))
    press("space")
    time.sleep(round(random.uniform(1.5, 1.75), 2))
    click(1501,917) 
    time.sleep(round(random.uniform(1.5, 1.75), 2))
    click(1501,917)
    time.sleep(round(random.uniform(1.5, 1.75), 2))
    click(1036,625)
    time.sleep(round(random.uniform(0.5, 0.75), 2))
    click(959,688, clicks=2)

def fishingCycle():
    pressFishingKey()
    time.sleep(4)
    text = getTextFromDialogue()
    #print(text)
    if "Pokémon" in text:
        press("space")
        log("Un Pokémon a mordu a l'hameçon!")
        time.sleep(11)
        log(f"{datetime.datetime.now().strftime('%H:%M:%S')} : Début d'un combat")
        lireDialogueCombat()
        while inFight():
            chat = lireDialogueCombat()
            if "plus de PP" in chat or "Miaouss est K.O" in chat:
                goToPokeCenter("Miaouss est K.O" in chat)
                break
            time.sleep(round(random.uniform(0.25, 0.75), 2))
            press("space", presses=2)
        log(f"{datetime.datetime.now().strftime('%H:%M:%S')} : Fin d'un combat")
        time.sleep(round(random.uniform(1, 1.5), 2))
        
    elif "rien" in text:
        press("space")  
        log("Rien de rien...")
        return 0
    
    else:
        log("Erreur lors du cycle de pêche")

def getTextFromDialogue():
    return pytesseract.image_to_string(pyautogui.screenshot(region=regionDialogue))

def inFight():
    with open("historiqueCombat.txt","r") as file:
        lines = file.readlines()
        return  not("$" in lines[-1] or "sac" in lines[-1])

def historiqueWrite(text):
    file = open("historiqueCombat.txt","a",  encoding="utf-8")
    file.write(text)
    file.close()

def historiqueRead():
    file = open("historiqueCombat.txt","r")
    lines = file.readlines()
    if lines == []: # Si dossier vide
        historiqueWrite(f"{datetime.datetime.now().strftime('%H:%M:%S')} : Création du fichier\n")
        historiqueWrite(f"{datetime.datetime.now().strftime('%H:%M:%S')} : Début du script\n")
        lines = file.readlines()
    file.close()
    return lines

def log(text):
    if historiqueRead()[-1] != text + "\n":
        historiqueWrite(text + '\n')
        print(text)

def lireDialogueCombat():
    screenshotChat = pyautogui.screenshot(region = regionChat)
    #screen.show()
    text = pytesseract.image_to_string(screenshotChat)
    nextLine = text
    nextLine = nextLine.replace("\n", "")
    lines = historiqueRead()
    lastLine = lines[len(lines)-1]
    if  lastLine != nextLine:
        log(nextLine)
    return text