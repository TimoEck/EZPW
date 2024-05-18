#Passwort Generator
import string
import random
import numpy as np


class PasswordGenerator:

    
    # def __init__(self) -> None:
    #     self.strings = string.ascii_letters
    #     self.lowerChar = string.ascii_lowercase
    #     self.upperChar = string.ascii_uppercase
    #     self.symbols = string.punctuation

    def set_Options():
       
        Auswahl = input("""
╔══════════════════════════════════════════════════╗
║ Treffen eine Auswahl:                            ║
║                                                  ║
║ [A] Kleinbuchstaben                              ║
║ [B] Klein- & Großbuchstaben                      ║
║ [C] Klein- & Großbuchstaben mit Zahlen           ║
║ [D] Top-Secret                                   ║
║                                                  ║
║                                 made by Timo Eck ║
╚══════════════════════════════════════════════════╝
""").upper()
        
        match Auswahl:
            case "A":
                charList = []
                optionList = string.ascii_lowercase
                for item in optionList:
                    charList.append(item)
                random.shuffle(charList)
                return charList 
            case "B":
                option = [string.ascii_lowercase , string.ascii_uppercase]
                charList = []
                optionList = string.ascii_lowercase +  string.ascii_uppercase
                for item in optionList:
                    charList.append(item)
                random.shuffle(charList)
                return charList 
             
            case "C":
                charList = []
                optionList = string.ascii_lowercase + string.ascii_uppercase + string.digits
                for item in optionList:
                    charList.append(item)
                random.shuffle(charList)    
                return charList            
            case "D":
                charList = []
                optionList = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
                for item in optionList:
                    charList.append(item)
                random.shuffle(charList)
                return charList 
            case _:
                print("Bitte treffe eine Auswahl.")


    def setLength(charList):
        Auswahl = int(input("""
╔══════════════════════════════════════╗
║ Bestimme die Länge deines Passworts: ║
╚══════════════════════════════════════╝
"""))
    
        try:
            np.array(charList)
            pwList = charList[:Auswahl]
            return pwList
        except TypeError as e:
            print(f"Es sind nur Ganzzahlen erlaubt. {e}")

    def createPassword(pwList):
        s = ""
        result = s.join(pwList)
        return result

PwGen = PasswordGenerator
option = PwGen.set_Options()
length = PwGen.setLength(option)
Password = PwGen.createPassword(length)
print(f"Passwort: {Password}")


