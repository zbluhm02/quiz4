from typing import Protocol
import math

class Father(Protocol):
    def __init__(self, assets1: int, assets2: int):
        self.assets1 = assets1
        self.assets2 = assets2
    
    def will(self):
        pass
class Son:
    def __init__(self, FAssets:int):
        self.FAssets = FAssets

    def will(self)->int:
        return self.FAssets


class Grandson(Father):
    def __init__(self, FAssets: int, GFAssets: int):
        self.FAssets = FAssets
        self.GFAssets = GFAssets
    def will(self)->int:
        return self.FAssets + self.GFAssets

son = Son(1500)
print("Will: $", son.will(), )

grandson = Grandson(-300, 1500)
print("Will: $", grandson.will())

