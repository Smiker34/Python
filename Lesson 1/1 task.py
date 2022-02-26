duration = int(input("Введите время "))
days = duration // 86400
sec = duration % 86400
hours = sec // 3600
sec %= 3600
min = sec // 60
sec %= 60
if min == 0:
    print(sec,"сек")
elif hours == 0:
    print (min,"мин",sec,"сек")
elif days == 0:
    print(hours,"час",min,"мин",sec,"сек")
else:
    print(days,"дн",hours,"час",min,"мин",sec,"сек")
