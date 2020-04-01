# 4. Определить, какое число в массиве встречается чаще всего.

import random

a = [random.randint(0, 10) for i in range(10)]
d_lst = {}
k_max = 0
tmp_key = 0

for id, item in enumerate(a):
    if item in d_lst:
        d_lst[item] += 1
    else:
        d_lst.update({item : 0})
        d_lst[item] += 1
    if k_max < d_lst[item]:
        tmp_key = item
        k_max = d_lst[item]

print(a)
print(f"Число, которое встречается больше всего раз: {tmp_key}, встретилось: {k_max} раз")
