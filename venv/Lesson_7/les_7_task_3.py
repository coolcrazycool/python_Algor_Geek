# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random


def med_finder(array):
    for id_f, value_f in enumerate(array):
        less_counter = 0
        bigger_counter = 0
        equal_counter = 0
        for id_s, value_s in enumerate(array):
            if id_f == id_s:
                continue
            elif value_f > value_s:
                bigger_counter += 1
            elif value_f < value_s:
                less_counter += 1
            else:
                equal_counter += 1
        if less_counter == len(array) // 2 and bigger_counter == len(array) // 2\
            or (less_counter + equal_counter) == len(array) // 2 and bigger_counter == len(array) // 2\
            or less_counter == len(array) // 2 and (bigger_counter + equal_counter) == len(array) // 2:
            return value_f


m = int(input("Введите m: "))
my_array = [random.uniform(0, 100) for i in range(2*m+1)]
print(my_array)

print(f'Медиана: {med_finder(my_array)}')
