from collections import deque


def zeroAdder(s_number, f_number):
    # выравнивание списков по кол-ву элементов с помощью незначащих нулей
    for i in range(abs(len(f_number) - len(s_number))):
        if len(f_number) > len(s_number):
            s_number.appendleft('0')
        else:
            f_number.appendleft('0')

def add(s_number, f_number, hex_dict):
    zeroAdder(s_number, f_number)
    sum_number = deque()
    for i in range(len(s_number) - 1, -1, -1):
        if i == len(f_number) - 1:
            abover = 0
        last_sum = hex_dict[f_number[i]] + hex_dict[s_number[i]] + abover
        abover = last_sum // 16
        last_sum %= 16
        for key, item in hex_dict.items():
            if item == last_sum:
                sum_number.appendleft(key)
                break
        if i == 0 and abover != 0:
            for key, item in hex_dict.items():
                if item == abover:
                    sum_number.appendleft(key)
                    break
    return sum_number

def mn(s_number, f_number, hex_dict):
    for i in range(len(s_number) - 1, -1, -1):
        que = deque()
        z_add = abs(i - len(s_number) + 1)
        for j in range(len(f_number) - 1, -1, -1):
            if j == len(s_number) - 1:
                mn = 0
            last_mn = hex_dict[f_number[j]] * hex_dict[s_number[i]] + mn
            mn = last_mn // 16
            last_mn %= 16
            for key, item in hex_dict.items():
                if item == last_mn:
                    que.appendleft(key)
                    break
            if j == 0 and mn != 0:
                for key, item in hex_dict.items():
                    if item == mn:
                        que.appendleft(key)
                        break
        for k in range(z_add):
            que.append('0')
        mn_number.append(que)
    while len(mn_number) > 1:
        mn_number[0] = add(mn_number[0], mn_number.pop(), hex_dict)
    return mn_number

#задание списков
f_number = deque(list(input("Первое число: ")))
s_number = deque(list(input("Второе число: ")))
mn_number = deque()

#кодировка
hex_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,\
            '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

#сложение
q_add = list(add(s_number, f_number, hex_dict))
print(q_add)

#умножение
q_mn = deque(list(*mn(s_number, f_number, hex_dict)))
while q_mn[0] == '0':
    q_mn.popleft()
q_mn = list(q_mn)
print(q_mn)
