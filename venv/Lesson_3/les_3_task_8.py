# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

a = [[0 for _ in range(0,4)] for _ in range(0,5)]

for i in range(0, 5):
    for j in range(0, 3):
        a[i][j] = int(input("Введите элемент: "))
        a[i][3] += a[i][j]

for i in a:
    for j in i:
        print(f"{j:>4}", end="")
    print()
