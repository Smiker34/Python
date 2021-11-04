class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, dir):
        print("Машина повернула", dir)

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышено скоростное ограничение")
        else:
            print(self.speed)

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышено скоростное ограничение")
        else:
            print(self.speed)

class PoliceCar(Car):
    pass

