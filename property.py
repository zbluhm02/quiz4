class Booty:
    def __init__(self, treasure, dubloons):
        self._treasure = treasure
        self._dubloons = dubloons

    @property
    def loot(self):
        return self._treasure, self._dubloons

    @loot.setter
    def loot(self, amount):
        self._treasure = self._treasure + amount
        self._dubloons = self._dubloons + amount

def main():
    
    
    pirate = Booty(10, 5)
    print ("Pirates Booty:", pirate.loot)
    
    pirate.loot = 2;
    print ("Pirates New Booty:", pirate.loot)

if __name__ == "__main__":
    main()