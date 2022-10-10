import math as m
import random

# flag = True
# while flag:
#     p, q = input("Введите два значения p и q: ").split()
#     try:
#         p = int(p)
#         q = int(q)
#     except ValueError:
#         print('')
#     else:
#         flag = False

p = 7
q = 11

n = p * q
f = (p - 1) * (q - 1)
ee = []
ee = [i for i in range(2, n) if m.gcd(i, i) == 1]
print(ee)


# random.randint(1, f - 1)
# dd = []
# print(n, f, e)
# for i in range(1000):
#     if i * e % f == 1:
#         # print(i)
#         dd.append(i)
# print(dd)
# d = dd[random.randint(0, len(dd))]
#
# print(dd)
#
# # d * 7 % 60 == 1:
# print(n, f, e)
#
# # def simple(a):
# #     k = 0
# #     for i in range(2, a // 2 + 1):
# #         if a % i == 0:
# #             k += 1
# #     if k == 0:
# #         return a
#
#
# # m = 111111
# # e = 3
# # d = 6111579
# # n = 9173503
#
# e = 3
# d = 7
# n = 33
#
# m = 31
# print(m)
# c = m ** e % n
# print(c)
# print(c ** d % n)
