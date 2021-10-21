def comp():
    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
    ]
    klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]
    for i in range(len(tutors)):
        try:
            yield (tutors[i],klasses[i])
        except IndexError:
            yield (tutors[i],"None")

pairs = comp()
while True:
    try:
        print(next(pairs))
    except StopIteration:
        break