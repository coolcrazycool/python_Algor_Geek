# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
import cProfile


def summa(n, sum=1, a=1):
    if n == 1:
        return sum
    b = a / -2
    sum += b
    return summa(n-1, sum, b)

# "les_2_task_4.summa(10)"
# 1000 loops, best of 5: 1.74 usec per loop

# "les_2_task_4.summa(100)"
# 1000 loops, best of 5: 20.3 usec per loop

# "les_2_task_4.summa(500)"
# 1000 loops, best of 5: 114 usec per loop

# "les_2_task_4.summa(800)"
# 1000 loops, best of 5: 191 usec per loop

# cProfile.run("summa(990)")

# 10/1    0.000    0.000    0.000    0.000 les_2_task_4.py:5(summa) 10

# 100/1    0.000    0.000    0.000    0.000 les_2_task_4.py:5(summa) 100

# 990/1    0.001    0.000    0.001    0.001 les_2_task_4.py:5(summa) 990
