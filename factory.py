class Warrior:
    def attack(self):
        print("Warrior")

class Mage:
    def attack(self):
        print("Mage")

class Archer:
    def attack(self):
        print("Archer")

class CharacterFactory:
    @staticmethod
    def choose_character(char_type):
        if char_type == "Warrior":
            return Warrior()
        elif char_type == "Mage":
            return Mage()
        elif char_type == "Archer":
            return Archer()
        else:
            print("Unknown")
            return None

choice = input("Choose your character: ")
player = CharacterFactory.choose_character(choice)

if player:
    player.attack()
