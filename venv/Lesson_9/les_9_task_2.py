# 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter
import heapq


def haff_alg(string_count):
    heap = [[count, [symbol, ""]] for symbol, count in string_count.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lower = heapq.heappop(heap)
        higher = heapq.heappop(heap)
        for pair in lower[1:]:
            pair[1] = '0' + pair[1]
        for pair in higher[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lower[0] + higher[0]] + lower[1:] + higher[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda i: (len(i[-1]), i))

s = input("Введите строку: ")
string_count = Counter(s)

haff_list = haff_alg(string_count)

out_list = ['Символ', 'Вес', 'Код']

print(f'{out_list[0]:>4}', f'{out_list[1]:>6}', f'{out_list[2]:>14}', sep=' ')
for i in haff_list:
    print(f'{i[0]:>5}', end=' ')
    print(f'{string_count[i[0]]:>7}', end=' ')
    print(f'{i[1]:>14}', end=' ')
    print()

print("Закодированная строка(пробелы между символами для наглядности):")
haff_dict = dict(haff_list)
for i in s:
    print(haff_dict[i],end=' ')