# Найти простое число на позиции n
import cProfile


def prime(n):
    id = 3
    i = 2

    if n == 0:
        return None
    if n == 1:
        return 2

    while True:
        flag = True
        for item in range(2, id):
            if id%item == 0:
                flag = False
                break
        if flag:
            if i == n:
                return id
            i += 1
        id += 1

# "Task_2_Ordinary.prime(10)"
# 1000 loops, best of 5: 14.4 usec per loop

# "Task_2_Ordinary.prime(100)"
# 1000 loops, best of 5: 1.4 msec per loop

# "Task_2_Ordinary.prime(200)"
# 1000 loops, best of 5: 6.43 msec per loop

# cProfile.run("prime(10000)")

# 1    0.000    0.000    0.000    0.000 Task_2_Ordinary.py:5(prime) 10

# 1    0.001    0.001    0.001    0.001 Task_2_Ordinary.py:5(prime) 100

# 1   29.468   29.468   29.468   29.468 Task_2_Ordinary.py:5(prime) 10000