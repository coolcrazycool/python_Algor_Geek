# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Принцип поиска медианы: она должна быть больше половины элементов и меньше половины элементов.
import random


def find_median(array):
    for index_f, value_f in enumerate(array):
        count_less = 0  # Задаём счётчик на меньше или равно
        count_more = 0  # Задаём счётчик на больше
        count_equal = 0  # Задаём счётчик на равенство
        for index_s, value_s in enumerate(array):
            if index_f == index_s:  # Чтобы не элемент не проверял сам себя, то сравниваем индексы, поэтому enumerate
                pass
            elif value_f < value_s:
                count_less += 1
            elif value_f > value_s:
                count_more += 1
            else:
                count_equal += 1
            if count_less > len(array) // 2 or count_more > len(array) // 2:  # Если элемент точно не медиана - break
                break
        # Проверка, чтобы не возвращал элемент от break
        if (count_less == len(array) // 2 and count_more == len(array) // 2) or \
                ((count_less + count_equal) == len(array) // 2 and count_more == len(array) // 2) or \
                (count_less == len(array) // 2 and (count_more + count_equal) == len(array) // 2):
            return value_f


BALANCE = 100  # Балансовый элемент, случайное число от 0 до BALANCE
len_of_array = int(input('Введите натуральное число m: '))
array_input = [random.random() * BALANCE for i in range(2 * len_of_array + 1)]
print(f'Исходный массив: {array_input}')
median = find_median(array_input)
print(f'Медиана в исходном массиве - это число: {median}')