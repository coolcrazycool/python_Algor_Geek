# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

k = [0 for i in range(2, 10)]

for item in range(2, 100):
    for krat in range(2, 10):
        if item%krat == 0:
            k[krat-2] += 1

for id, item in enumerate(k):
    print(f"Кратно {id+2}: {item}")
