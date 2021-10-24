result = []
with open("nginx_logs.txt") as file:

    for line in file:
        r_addr = line[:line.find(" ") + 1]
        work_point = line.find('"')
        r_type = line[work_point + 1: line.find(' ', work_point)]
        work_point = line.find(' ', work_point)
        r_resource = line[work_point + 1: line.find(' ', work_point + 1)]
        result.append((r_addr, r_type, r_resource))

print(*result, sep = "\n", file = open("result.txt", "w"))