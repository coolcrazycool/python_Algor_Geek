# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

n = int(input("Введите n: "))
sum_alt = n*(n+1)/2
summa = 0

while n > 0:
    summa += n
    n -= 1

if sum_alt == summa:
    print(f"{summa} == {sum_alt}")
else:
    print(f"{summa} != {sum_alt}")