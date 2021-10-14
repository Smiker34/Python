def num_translate(num):
    translate = {'one': "один", 'two': "два", 'three': "три", 'four': "четыре", 'five': "пять",
                 'six': "шесть", 'seven': "семь", 'eight': "восемь", 'nine': "девять", 'ten': "десять"}
    print(translate.get(num.lower(),None))

num = input("Введите слово: ")
num_translate(num)