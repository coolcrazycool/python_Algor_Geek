'''
2. Закодируйте любую строку по алгоритму Хаффмана.
'''
from heapq import heappush, heappop, heapify
from collections import Counter


def encode(symb2freq):
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

if __name__ == "__main__":
    while True:
        s = input('Введите строку: ')
        if len(s) == 0:
            print('Строка не может быть пустой!')
            continue
        symb2freq = Counter(s)
        huff = encode(symb2freq)
        print("Symbol\tWeight\tHuffman Code")
        for p in huff:
            print(f'{p[0]:>5}', end=' ')
            print(f'{symb2freq[p[0]]:>7}', end=' ')
            print(f'{p[1]:>14}', end=' ')
            print()
        break
