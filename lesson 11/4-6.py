import re


class Warehouse():
    storing = {"Printers": [], "Scanners": [], "Copiers": []}

    def tech_get(self,name, num):
        if name == "printer":
            for i in range(num):
                self.storing["Printers"].append(Printer.all_printers[i-1])
                Printer.all_printers.pop(i-1)
        if name == "scanner":
            for i in range(num):
                self.storing["Scanners"].append(Scanner.all_scanners[i - 1])
                Scanner.all_scanners.pop(i - 1)
        if name == "copier":
            for i in range(num):
                self.storing["Copiers"].append(Copier.all_copiers[i - 1])
                Copier.all_copiers.pop(i - 1)
        return self.storing

    def send(self,name):
        all_techs = self.storing.values()
        for subj in all_techs:
            for names in subj:
                for tech in name:
                    if tech in names:
                        subj.remove(names)
                        print(tech, "Отправлен")


class Tech():

    def __init__(self,name, price):
        self.name = name
        self.price = price


class Printer(Tech):

    all_printers = []

    def __init__(self, name, price, color):
        Tech.__init__(self, name, price)
        self.print_color = color
        self.all_printers.append({self.name: [self.price, self.print_color]})


class Scanner(Tech):

    all_scanners = []

    def __init__(self, name, price, type):
        Tech.__init__(self, name, price)
        self.type = type
        self.all_scanners.append({self.name: [self.price, self.type]})


class Copier(Tech):

    all_copiers = []

    def __init__(self, name, price, size):
        Tech.__init__(self, name, price)
        self.size = size
        self.all_copiers.append({self.name: [self.price, self.size]})


while True:
    ware = Warehouse()
    command = input("Введите команду: ").lower()

    if command == "add tech":
        while True:
            techs = ["printer", "scanner", "copier"]
            tech = input("Введите название техники (printer, scanner, copier): ").lower()
            if tech not in techs:
                print("Некорректные данные")
            else:
                break
        while True:
            if tech == "printer":
                params = input("Введите название, цену и цвет печати через запятую: ").split(",")
                if len(params) < 3:
                    print("Нехватает данных")
                else:
                    printer = Printer(params[0], params[1], params[2])
                    print("Добавлено")
                    break

            if tech == "scanner":
                params = input("Введите название, цену и тип через запятую: ").split(",")
                if len(params) < 3:
                    print("Нехватает данных")
                else:
                    scanner = Scanner(params[0], params[1], params[2])
                    print("Добавлено")
                    break

            if tech == "scanner":
                params = input("Введите название, цену и тип через запятую: ").split(",")
                if len(params) < 3:
                    print("Нехватает данных")
                else:
                    copier = Copier(params[0], params[1], params[2])
                    print("Добавлено")
                    break

    if command == "to warehouse":
        while True:
            techs = ["printer", "scanner", "copier"]
            tech = input("Введите название техники (printer, scanner, copier): ").lower()
            if tech not in techs:
                print("Некорректные данные")
            else:
                break
        while True:
            num = input("Сколько отправить на склад: ")
            if re.search("\D", num):
                print("Некорректные данные")
            else:
                num = int(num)
                break
        try:
            ware.tech_get(tech,num)
            print("Доставлено на склад")
        except Exception:
            print("Доставлено сколько возможно")

    if command == "check warehouse":
        print(ware.storing)

    if command == "send tech":
        names = input("Введите через запятую имена отправляемой техники: ").split(",")
        ware.send(names)
        print("Отправлено")

    if command == "help":
        print("'add tech' - добавление техники.")
        print("'to warehouse' - отправка техники на склад.")
        print("'check warehouse' - проверка склада.")
        print("'send tech' - отправка техники со склада.")
        print("'stop' - завершить выполнение.")

    if command == "stop":
        break

    else:
        print("Введите 'help' для получения списка команд")