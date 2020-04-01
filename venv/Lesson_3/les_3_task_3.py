# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = [random.randint(0, 100) for i in range(10)]
max_num = [a[0], 0]
min_num = [a[0], 0]

for id, item in enumerate(a):
    if item > max_num[0]:
        max_num = [item, id]
    if item < min_num[0]:
        min_num = [item, id]

print(f"Список старый: {a}")
a[max_num[1]], a[min_num[1]] = a[min_num[1]], a[max_num[1]]
print(f"Список новый: {a}")
