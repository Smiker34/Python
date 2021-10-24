from sys import argv
param = argv[1:]

if len(param) < 1:
    with open("bakery.csv", encoding="utf-8") as file:
        print(file.read())

if len(param) == 1:
    with open("bakery.csv", encoding="utf-8") as file:
        file.seek(0)
        text = file.readlines()[int(param[0]) - 1:]
        for arg in text:
            print(arg.strip("\n"))

if len(param) == 2:
    with open("bakery.csv", encoding="utf-8") as file:
        file.seek(0)
        text = file.readlines()[int(param[0]) - 1:int(param[1])]
        for arg in text:
            print(arg.strip("\n"))
else:
    print("Некорректные параметры")