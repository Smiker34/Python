from sys import argv
sale = argv[1:]
if len(sale) < 1:
    print("Нет значений")
for arg in range(len(sale)):
    print(sale[arg], file=open("bakery.csv", "a", encoding="utf-8"))