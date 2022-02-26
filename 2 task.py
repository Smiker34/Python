list = []
for ind in range(1001):
    if ind % 2 != 0:
        list.append(ind**3)

total_sum1 = 0
for ind in list:
    sum = 0
    number = ind
    while ind != 0:
        sum = sum + ind % 10
        ind = ind // 10
    if sum % 7 == 0:
        total_sum1 += number
print(total_sum1)

total_sum2 = 0
for ind in list:
    sum = 0
    ind += 17
    number = ind
    while ind != 0:
        sum = sum + ind % 10
        ind = ind // 10
    if sum % 7 == 0:
        total_sum2 += number
print(total_sum2)

