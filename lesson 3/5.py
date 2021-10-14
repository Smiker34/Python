from random import choice
def get_jokes(num):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if rep == "Y":
        while num > 0:
            joke = []
            joke.append(choice(nouns))
            joke.append(choice(adverbs))
            joke.append(choice(adjectives))
            print(" ".join(joke))
            num -= 1
    else:
        try:
            while num > 0:
                joke = []
                first_word = choice(nouns)
                nouns.remove(first_word)
                second_word = choice(adverbs)
                adverbs.remove(second_word)
                third_word = choice(adjectives)
                adjectives.remove(third_word)
                joke.append(first_word)
                joke.append(second_word)
                joke.append(third_word)
                print(" ".join(joke))
                num -= 1
        except IndexError:
            print("\n","Шутки кончились")

try:
    num = int(input("Введите число: "))
except ValueError:
    while True:
        try:
            num = int(input("Введите число:"))
        except ValueError:
            continue
        else:
            break
rep = input("Разрешить повтор? (Y/N):")
if not(rep == "Y" or rep == "N"):
    while True:
        rep = input("Введите корректно (Y/N):")
        if rep == "Y" or rep == "N":
            break
print("\n")
get_jokes(num)