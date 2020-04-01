# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

a = [random.randint(0, 100) for i in range(10)]
max_num = [a[0], 0]
min_num = [a[0], 0]
summa = 0

for id, item in enumerate(a):
    if item > max_num[0]:
        max_num = [item, id]
    if item < min_num[0]:
        min_num = [item, id]

if max_num[1] < min_num[1]:
    max_num[1], min_num[1] = min_num[1], max_num[1]

for index in range(min_num[1]+1, max_num[1]):
    summa += a[index]

print(a)
print(f"Сумма между максимальным и минимальным: {summa}")