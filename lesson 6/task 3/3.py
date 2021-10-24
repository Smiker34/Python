with open("users.csv", encoding='utf-8') as file:
    users = []
    for line in file:
        user = line.replace(",", " ")
        if user.find("\n") != -1:
            user = user[:user.find("\n")]
        users.append(user)

with open("hobby.csv", encoding='utf-8') as file:
    hobbies = []
    for line in file:
        hobby = line.replace(",", ", ")
        if hobby.find("\n") != -1:
            hobby = hobby[:hobby.find("\n")]
        hobbies.append(hobby)

if len(hobbies) > len(users):
    exit(1)
result = {}
for i in range(len(users)):
    result[users[i]] = hobbies[i]
print(result)