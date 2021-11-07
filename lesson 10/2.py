from abc import ABC, abstractmethod
class Clothes(ABC):
    @abstractmethod
    def needed_cloth(self):
        pass

class Coat(Clothes):
    def __init__(self,size):
        self.size = size

    @property
    def needed_cloth(self):
        return round(self.size / 6.5 + 0.5, 2)

class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def needed_cloth(self):
        return self.height * 2 + 0.3

coat = Coat(64)
costume = Costume(170)
result = round(coat.needed_cloth + costume.needed_cloth, 2)
print(result)