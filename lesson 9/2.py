class Road():
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass_calculate(self):
        mass = self._width * self._lenght * 25 * 5
        return mass

road = Road(5000, 20)
print(road.mass_calculate())