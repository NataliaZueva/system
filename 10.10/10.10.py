def file_read(title):
    a = []
    b = open(title, 'r').readlines()
    for line in b:
        a.append([int(x) for x in line.split()])
    return a


a = file_read('text.txt')

b = []
for i in range(a[0][0]):
    b.append([0 for i in range(a[0][0])])

for i in range(1, len(a)):
    b[(a[i])[0] - 1][(a[i])[1] - 1] = 1
print(b)