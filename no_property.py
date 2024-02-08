class Booty:
    def __init__(self, treasure, dubloons):
        self._treasure = treasure
        self._dubloons = dubloons

    def get_loot(self):
        return self._treasure, self._dubloons

    def set_loot(self, amount):
        self._treasure = self._treasure + amount
        self._dubloons = self._dubloons + amount

    loot = property(get_loot, set_loot)

def main():
    pirate = Booty(10, 5)
    print("Pirate's Booty:", pirate.loot)
    
    pirate.loot = 2
    print("Pirate's New Booty:", pirate.loot)

if __name__ == "__main__":
    main()