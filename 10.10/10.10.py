def file_read(title):
    a = []
    b = open(title, 'r').readlines()
    for line in b:
        a.append([int(x) for x in line.split()])
    return a

a = file_read('text.txt')


v = 4
b = []
for i in range(v):
    b.append([0 for i in range(v)])
print(b)

for i in range(1, len(a)):
    v = a[i]
    print(v)
    b[v[0]-1][v[1]-1] = 1
print(b)



# print(a[0])
# # def pr():
#
# b = []
# for i in range(a[0][0]):
#     for j in range(a[0][0]):
#         if a[i+1][]
#         b.append(0)
#     b.append("\n")
#
# print(b)