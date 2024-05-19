#Passwort Generator
import string
import random
import numpy as np


class PasswordGenerator:

    #Initialize length and character-set
    def __init__(self, length = 8, character_set = "") -> None:
        self.length = length
        self.character_set = character_set

    #Input set Option which character-set will be used
    def set_Options(self):
       
        selection = input("""
╔══════════════════════════════════════════════════╗
║ Choose Security-Level (Default is [B]):          ║
║                                                  ║
║ [A] Lowercases                                   ║
║ [B] Lower- & Uppercase                           ║
║ [C] Lower- & Uppercase with digits               ║
║ [D] Top-Secret                                   ║
║                                                  ║
║                                 made by Timo Eck ║
╚══════════════════════════════════════════════════╝
""").upper()
        
        
        if selection == "" or selection == "B":
                self.character_set = string.ascii_lowercase
        elif selection == "B":
                self.character_set = string.ascii_lowercase +  string.ascii_uppercase
        elif selection == "C":
                self.character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits     
        elif selection == "D":
                self.character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        else:
            print("Please make a valid selection.")
            return self.set_Options()

    # Input set length how many characters will be used
    def set_Length(self):
        try:
            self.length = int(input("Password length:"))
        except ValueError:
            print("Enter a valid Number.")
            self.set_Length()
    
    #Generate password with random selection from character-set for selected length 
    def generatePassword(self):
        if not self.character_set:
            print("Character set is empty. Please set the options.")
            return None
        password = "".join(random.choice(self.character_set) for _ in range(self.length))
        return password

PwGen = PasswordGenerator()
option = PwGen.set_Options()
length = PwGen.set_Length()
Password = PwGen.generatePassword()
print(f"Generated Password: {Password}")


