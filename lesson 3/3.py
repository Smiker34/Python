def thesaurus(names):
    staff = {}
    for name in names:
        name = name.title()
        if staff.get(name[0]) is None:
            staff[name[0]] = [name]
        else:
            staff[name[0]].append(name)
    return staff
names = input("Введите имена через пробел: ").split()
for key, value in thesaurus(names).items():
    print("{}: {}".format(key, value))