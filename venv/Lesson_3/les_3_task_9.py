# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

height = 5
width = 5
matrix = [[random.randint(1, 100) for _ in range(height)] for _ in range(width)]
max_of_min = 0

for line in matrix:
    for pos in line:
        print(f"{pos:>4}", end="")
    print()

for id in range(width):
    min_num = matrix[0][id]
    for column in range(height):
        if matrix[column][id] < min_num:
            min_num = matrix[column][id]
    if min_num > max_of_min:
        max_of_min = min_num

print(f"Максимальное среди минимальных: {max_of_min}")