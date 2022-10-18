def file_read(title):
    a = []
    b = open(title, 'r').readlines()
    for line in b:
        a.append([int(x) for x in line.split()])
    return a


a = file_read('text1.txt')
b = file_read('text2.txt')
s = open('answer.txt', 'w')
c = [a, b]
f = 1
for mac in c:
    N, E = mac[0][0], mac[0][1]

    new_dict = {}
    for i in range(1, N + 1):
        new_dict[i] = 0

    for i in range(1, E + 1):
        new_dict[mac[i][0]] += 1
        new_dict[mac[i][1]] += 1
    res = []
    for key in new_dict.keys():
        res.append(new_dict[key])
    s.write(f"Задача №{f}: \n")
    for i in res:
        s.write(str(i) + ' ')
    s.write("\n\n")
    f += 1

s.close()
