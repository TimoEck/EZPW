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
        while True:
           
            selection = input("""
    ╔══════════════════════════════════════════════════╗
    ║ Choose Security-Level (Default is [B]):          ║
    ║                                                  ║
    ║ [A] Lowercases                                   ║
    ║ [B] Lower- & Uppercase                           ║
    ║ [C] Lower- & Uppercase with digits               ║
    ║ [D] Top-Secret                                   ║
    ║ [E] Close application                            ║
    ║                                                  ║
    ║                                 made by Timo Eck ║
    ╚══════════════════════════════════════════════════╝
    """).upper()
            
            
            if selection == "" or selection == "B":
                    self.character_set = string.ascii_lowercase +  string.ascii_uppercase
            elif selection == "A":
                    self.character_set = string.ascii_lowercase
            elif selection == "C":
                    self.character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits     
            elif selection == "D":
                    self.character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            elif selection == "E":
                    exit() 
            else:
                print("Please make a valid selection.")
                continue
            break

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




if __name__ == "__main__":
    while True:
        pw_gen = PasswordGenerator()
        pw_gen.set_Options()
        pw_gen.set_Length()
        password = pw_gen.generatePassword()
        if password:
            print(f"Generated password: {password}")

        another = input("Generate another password? (Y/N): ").upper()
        if another != 'Y':
            break


