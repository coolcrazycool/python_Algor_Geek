# Найти простое число на позиции n
import math
import cProfile


def sieve(n):
    if n == 0:
        return None
    if n == 1:
        return 2

    foundedPrimes = 0
    sieve_list = [True for i in range(int(round(2 * n * math.log(2 * n))))]
    primeSieve = []

    while True:
        if foundedPrimes == 0:
            iter = 2
        else:
            iter = sieve_list[foundedPrimes-1] + 2
        for i in range(iter, len(sieve_list)):
            if sieve_list[i] == True:
                primeSieve.append(i)
                foundedPrimes += 1
                if foundedPrimes == n:
                    break
                for j in range(i + i, len(sieve_list), i):
                    sieve_list[j] = False
            else:
                continue
        if foundedPrimes == n:
            break
    return primeSieve[n-1]

# print(sieve(10000))

# "Task_2_Eratosfen.eratosthenes(10)"
# 1000 loops, best of 5: 10 usec per loop

# "Task_2_Eratosfen.eratosthenes(100)"
# 1000 loops, best of 5: 194 usec per loop

# "Task_2_Eratosfen.eratosthenes(1000)"
# 1000 loops, best of 5: 2.92 msec per loop

# "Task_2_Eratosfen.eratosthenes(10000)"
# 1000 loops, best of 5: 46.2 msec per loop

# cProfile.run("sieve(1000)")

# 1    0.000    0.000    0.000    0.000 Task_2_Eratosfen.py:5(sieve) 100

# 1    0.003    0.003    0.004    0.004 Task_2_Eratosfen.py:5(sieve) 1000

# 1    0.041    0.041    0.055    0.055 Task_2_Eratosfen.py:5(sieve) 10_000

# 1    8.439    8.439   10.564   10.564 Task_2_Eratosfen.py:5(sieve) 1_000_000