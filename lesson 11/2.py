class ZeroDivision(Exception):
    pass


while True:

    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))

    if b == 0:
        try:
            raise ZeroDivision
        except ZeroDivision:
            print("Попытка деления на ноль")
    else:
        print(a / b)