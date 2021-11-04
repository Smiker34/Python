class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):

    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):

    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):

    def draw(self):
        print("Запуск отрисовки маркером")

stationery = Stationery("title")
stationery.draw()

stationery = Pen("title")
stationery.draw()

stationery = Pencil("title")
stationery.draw()

stationery = Handle("title")
stationery.draw()