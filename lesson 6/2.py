IPs = {}
with open("nginx_logs.txt") as file:

    for line in file:
        ip = line[:line.find(" ") + 1]
        if ip in IPs:
            value = IPs.get(ip) + 1
            IPs[ip] = value
        else:
            IPs[ip] = 1
print(max(IPs, key=IPs.get), max(IPs.values()))
