from random import uniform

def transform(value):
    rub = int(value // 1)
    kop = int(round(value % 1, 2) * 100)
    kop = str(kop)
    if len(kop) < 2:
        kop = "0" + kop
    return rub, kop

prices = []
for i in range(20):
    prices.append(round(uniform(10,100),2))
print("Изначальные данные")
print(prices)

# Вывод списком
print("\n", "Вывод списком")
for i in prices:
    rub,kop = transform(i)
    print(rub, "руб", kop, "коп", end=",")

# Сортированный по возрастанию
print("\n"*2, "Сортированный по возрастанию")
prices.sort()
for i in prices:
    rub,kop = transform(i)
    print(rub, "руб", kop, "коп", end=",")

# Сортированный по убыванию
print("\n"*2, "Сортированный по убыванию")
prices.sort(reverse=True)
for i in prices:
    rub,kop = transform(i)
    print(rub, "руб", kop, "коп", end=",")

# 5 Самых дорогих
print("\n"*2, "5 Самых дорогих")
prices.sort(reverse=True)
prices = prices[:5]
for i in prices:
    rub,kop = transform(i)
    print(rub, "руб", kop, "коп", end=",")
