def num_translate_adv(num):
    translate = {'one': "один", 'two': "два", 'three': "три", 'four': "четыре", 'five': "пять",
                 'six': "шесть", 'seven': "семь", 'eight': "восемь", 'nine': "девять", 'ten': "десять"}
    if num.istitle() or num.isupper():
        print((translate.get(num.lower(), None)).title())
    else:
        print(translate.get(num.lower(),None))

num = input("Введите слово: ")
num_translate_adv(num)