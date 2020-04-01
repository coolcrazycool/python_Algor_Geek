# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

a = [random.randint(-100, 100) for i in range(10)]
index = 0
max_negative = 0

for id, item in enumerate(a):
    if item < 0:
        if max_negative == 0:
            max_negative = item
            index = id
        elif item > max_negative:
            max_negative = item
            index = id

print(a)
if max_negative == 0:
    print(f"Отрицательных чисел нет")
else:
    print(f"Максимальное отрицательное {max_negative} находится на {index} позиции")
