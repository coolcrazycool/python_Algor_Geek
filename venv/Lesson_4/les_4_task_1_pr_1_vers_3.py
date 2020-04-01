# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
import cProfile


def summ_list(n):
    item = 1
    summ_l = [None] * 1000
    summ_l[:2] = [0, 1]

    def _summ_list(n):
        if summ_l[n] is None:
            summ_l[n] = summ_l[1] / pow(-2, n-1) + _summ_list(n - 1)
            return summ_l[n]

        return summ_l[n]

    return _summ_list(n)

# "les_4_task_1_pr_1_vers_3.summ_list(10)"
# 1000 loops, best of 5: 10.8 usec per loop

# "les_4_task_1_pr_1_vers_3.summ_list(100)"
# 1000 loops, best of 5: 80.9 usec per loop

# "les_4_task_1_pr_1_vers_3.summ_list(500)"
# 1000 loops, best of 5: 552 usec per loop

# "les_4_task_1_pr_1_vers_3.summ_list(900)"
# 1000 loops, best of 5: 1.17 msec per loop

# "les_4_task_1_pr_1_vers_3.summ_list(988)"
# 1000 loops, best of 5: 1.39 msec per loop

# cProfile.run("summ_list(980)")

# 10/1    0.000    0.000    0.000    0.000 les_4_task_1_pr_1_vers_3.py:10(_summ_list) 10

# 100/1    0.000    0.000    0.000    0.000 les_4_task_1_pr_1_vers_3.py:10(_summ_list) 100

# 500/1    0.001    0.000    0.001    0.001 les_4_task_1_pr_1_vers_3.py:10(_summ_list) 500

# 980/1    0.002    0.000    0.004    0.004 les_4_task_1_pr_1_vers_3.py:10(_summ_list) 980

