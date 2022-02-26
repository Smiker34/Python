staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in staff:
    staffer = i.split(" ")
    print("Привет, %s!"%(staffer[len(staffer)-1].title()))
print(staff)
