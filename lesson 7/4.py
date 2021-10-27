import os

files = os.listdir(os.getcwd())
sizes = []
for file in files:
    sizes.append(os.stat(os.path.join(os.getcwd(), file)).st_size)

sizes = sorted(sizes)
min_lim = 10 ** len(str(sizes[0]))

result = {}
score = 0
for size in sizes:
    if size < min_lim:
        score += 1
        result[min_lim] = score
    else:
        while True:
            min_lim *= 10
            if size < min_lim:
                break
        score = 1
        result[min_lim] = score

for key, value in result.items():
    print("{0}: {1}".format(key, value))