# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(array):
    if len(array) < 2:
        return array

    left = merge_sort(array[:len(array)//2])
    right = merge_sort(array[len(array)//2:])

    i = j = 0
    result = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            result.append(right[j])
            j += 1
        elif not j < len(right):
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result

N = 10
my_array = [random.uniform(0, 49) for i in range(N)]
print(my_array)

print(merge_sort(my_array))
