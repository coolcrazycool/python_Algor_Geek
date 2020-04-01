# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
import cProfile


def summa(n):
    summ = 0
    item = 1
    for i in range(n):
        summ += item
        item /= -2
    return summ

# "les_4_task_1_pr_1_vers_2.summa(10)"
# 1000 loops, best of 5: 975 nsec per loop

# "les_4_task_1_pr_1_vers_2.summa(100)"
# 1000 loops, best of 5: 6.62 usec per loop

# "les_4_task_1_pr_1_vers_2.summa(500)"
# 1000 loops, best of 5: 32.9 usec per loop

# "les_4_task_1_pr_1_vers_2.summa(1000)"
# 1000 loops, best of 5: 68.6 usec per loop

# "les_4_task_1_pr_1_vers_2.summa(5000)"
# 1000 loops, best of 5: 368 usec per loop

# cProfile.run("summa(100000)")

# 1    0.000    0.000    0.000    0.000 les_4_task_1_pr_1_vers_2.py:5(summa) 10

# 1    0.000    0.000    0.000    0.000 les_4_task_1_pr_1_vers_2.py:5(summa) 100

# 1    0.001    0.001    0.001    0.001 les_4_task_1_pr_1_vers_2.py:5(summa) 10_000

# 1    0.008    0.008    0.008    0.008 les_4_task_1_pr_1_vers_2.py:5(summa) 100_000