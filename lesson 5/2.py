try:
    max_num = int(input("Введите предел генерации: "))
except ValueError:
    print("Введено не число")
    exit()
numbers = (i for i in range(max_num+1) if i % 2 != 0)
while True:
    try:
        print(next(numbers))
    except StopIteration:
        break
