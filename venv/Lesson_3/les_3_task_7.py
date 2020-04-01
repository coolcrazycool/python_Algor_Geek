# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба минимальны), так и различаться.

import random

a = [random.randint(-10, 10) for i in range(10)]
prev_min = a[0]
min_num = a[0]

for id, item in enumerate(a):
    if item <= min_num:
        prev_min = min_num
        min_num = item

print(a)
print(f"Минимальное первое: {min_num}, второе: {prev_min}")
