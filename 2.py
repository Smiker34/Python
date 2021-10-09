info = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_info = []
for i in info:
    if i.isdigit():
        if len(i) < 2:
            i = "0" + i[:1]
        new_info.append('"')
        new_info.append(i)
        new_info.append('"')
    elif i.find("+") == 0 or i.find("-") == 0:
        if i[1:].isdigit():
            if len(i) < 3:
                i = i[:1] + "0" + i[1:]
            new_info.append('"')
            new_info.append(i)
            new_info.append('"')
    else:
        new_info.append(i)
sentence = ""
sentence += " ".join(new_info)
open = True   # Открытие/закрытие кавычек
move = 0      # Сдвиг индексов
for ind,val in enumerate(sentence):
    if val == '"':
        if open == True:
            sentence = sentence[:ind+1-move] + sentence[ind+2-move:]
            open = False
            move += 1
        else:
            sentence = sentence[:ind-1-move] + sentence[ind-move:]
            open = True
            move += 1
print(sentence)