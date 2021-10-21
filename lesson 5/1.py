def num_gen(max_num):
    number = 1
    while number < max_num:
        yield number
        number += 2
try:
    max_num = int(input("Введите предел генерации: "))
except ValueError:
    print("Введено не число")
    exit()
numbers = num_gen(max_num)
while True:
    try:
        print(next(numbers))
    except StopIteration:
        break
