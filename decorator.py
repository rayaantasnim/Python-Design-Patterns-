class Character:
    def description(self):
        return "Basic Character"
    def stats(self):
        print("Health: 100")
        print("Attack: 20")
        print("Speed: 5")
class CharacterDecorator:
    def __init__(self, character):
        self.character = character
    def description(self):
        return self.character.description()
    def stats(self):
        self.character.stats()
class ShieldDecorator(CharacterDecorator):
    def description(self):
        return self.character.description() + " + Shield"
    def stats(self):
        self.character.stats()
        print("Shield: +50 Defense")

class PowerDecorator(CharacterDecorator):
    def description(self):
        return self.character.description() + "+ Power"
    def stats(self):
        self.character.stats()
        print("Attack Boost: +15")

class SpeedDecorator(CharacterDecorator):
    def description(self):
        return self.character.description() + "+ Speed"

    def stats(self):
        self.character.stats()

player = Character()
print("==== Basic Character ====")
print(player.description())
player.stats()

print("\n==== Add Sheild ====")
player = ShieldDecorator(player)