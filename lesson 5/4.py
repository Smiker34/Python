from random import randint
count = randint(1,15)
src = []
for i in range(count):
    src.append(randint(1,1000))
result = [src[i] for i in range(1,len(src)) if src[i]>src[i-1]]
print(src)
print(result)