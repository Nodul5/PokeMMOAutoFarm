# USING UTF-8

from pyautogui import *
import pytesseract, pyautogui, datetime, time, random, tkinter

tk = tkinter.Tk()
regionChat = (5,1140,395,20)
regionDialogue = (550,140,700,120)
screenResolution = [tk.winfo_screenwidth(),tk.winfo_screenheight()]
screenCenter = [screenResolution[0]//2, screenResolution[1]//2]
switchDeuxièmePokemon = (614,805)
fishingKey = '"'
bindAbra = "9"

totalEarnings = []
sac = {}

momentDebut = str(datetime.datetime.now())


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def updateStats(money = 0,drop = ""):
    global totalEarnings
    global sac
    if drop != "":
        if (drop in sac):
            sac[drop] += 1
        elif not(drop in sac):
            sac[drop] = 1
    totalEarnings = totalEarnings + [money]
    with open("earnings.txt","w") as file:
        file.write(f"{momentDebut}\n")
        for drop in sac.keys():
            file.write(f"{drop} : {sac[drop]}\n")
        file.write(f"Total money : {sum(totalEarnings)}\n")
    
def pressFishingKey():
    press(fishingKey)

def isOnScreen(image):
    positions = locateOnScreen(image, confidence=1)
    return positions != None  

def goToPokeCenter(dead = False):
    if dead:
        click(switchDeuxièmePokemon[0],switchDeuxièmePokemon[1]) #Switch sur deuxieme pokemon
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
    time.sleep(round(random.uniform(6.5, 6.75), 2))
    press("space")
    time.sleep(round(random.uniform(1.5, 1.75), 2))
    press("space")
    time.sleep(round(random.uniform(1.5, 1.75), 2))
    keyDown("shift")
    keyDown("s")
    time.sleep(3.5)
    keyUp("s")
    keyDown("q")
    time.sleep(1.25)
    keyUp("q")
    keyDown("s")
    time.sleep(2)
    keyUp("s")
    keyUp("shift")

def fishingCycle():
    pressFishingKey()
    time.sleep(4)
    text = getTextFromDialogue()
    if "Pokémon" in text:
        retirerObjet = False
        press("space")
        log("Un Pokémon a mordu a l'hameçon!")
        time.sleep(11)
        log(f"{datetime.datetime.now().strftime('%H:%M:%S')} : Début d'un combat")
        lireDialogueCombat()
        while inFight():
            chat = lireDialogueCombat()
            if "plus de PP" in chat or "Miaouss est K.O" in chat:
                goToPokeCenter("Miaouss est K.O" in chat)
                return 0
            elif "Vous avez trouvé" in chat:
                updateStats(money = 0, drop=chat.split("un ")[1].split("!"))
            time.sleep(round(random.uniform(0.25, 0.75), 2))
            press("space", presses=2)
        chat = lireDialogueCombat()
        if ("$" in chat):
            updateStats(money = int(chat.split("obtient ")[1].split(" $")[0]), drop="")
        time.sleep(round(random.uniform(1, 1.5), 2))
        chat = lireDialogueCombat()
        log(f"{datetime.datetime.now().strftime('%H:%M:%S')} : Fin d'un combat")
        if "sac" in chat:
            updateStats(money = 0, drop=chat.split("a mis le ")[1].split(" dans")[0])
    elif "rien" in text:
        press("space")  
        log("Rien de rien...")
        return 0
    
    else:
        log("Erreur lors du cycle de pêche")
        return 0

def getTextFromDialogue():
    image = pyautogui.screenshot(region=regionDialogue)
    image.save("temp.png")
    text = pytesseract.image_to_string(image)
    return text

def inFight():
    with open("historiqueCombat.txt","r") as file:
        lines = file.readlines()
        return  not("$" in lines[-1] or "sac" in lines[-1])

def historiqueWrite(text):
    file = open("historiqueCombat.txt","a",  encoding="utf-8")
    file.write(text)
    file.close()

def historiqueRead():
    file = open("historiqueCombat.txt","r", encoding='utf-8', errors='ignore')
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