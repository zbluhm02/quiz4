from abc import ABC, abstractmethod
import math

class Father(ABC):
    @abstractmethod
    def will(self):
        pass


class Son(Father):
    def __init__(self, FAssets):
        self.FAssets = FAssets

    def will(self):
        return self.FAssets


class Grandson(Father):
    def __init__(self, FAssets, GFAssets):
        self.FAssets = FAssets
        self.GFAssets = GFAssets
    def will(self):
        return self.FAssets + self.GFAssets


# Example usage
son = Son(1000)
print("Son's Will: $", son.will(), )

grandson = Grandson(1000, 2500)
print("Grandson's Will: $", grandson.will())
