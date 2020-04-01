# Складывает и умножает 2 числа в 16-ичной системе счисления

from collections import deque
import sys


def show_size(x, level=0):
    result_size = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                result_size += show_size(key, level + 1)
                result_size += show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                result_size += show_size(item, level + 1)
    return result_size

def zeroAdder(s_number, f_number):
    # выравнивание списков по кол-ву элементов с помощью незначащих нулей
    for i in range(abs(len(f_number) - len(s_number))):
        if len(f_number) > len(s_number):
            s_number.appendleft('0')
        else:
            f_number.appendleft('0')

def add(s_number, f_number):
    zeroAdder(s_number, f_number)
    sum_number = deque()
    for i in range(len(s_number) - 1, -1, -1):
        if i == len(f_number) - 1:
            abover = 0
        last_sum = hex_dict[f_number[i]] + hex_dict[s_number[i]] + abover
        abover = last_sum // 16
        last_sum %= 16
        sum_number.appendleft(dec_dict[last_sum])
        if i == 0 and abover != 0:
            sum_number.appendleft(dec_dict[abover])
    return sum_number

def mn(s_number, f_number):
    for i in range(len(s_number) - 1, -1, -1):
        que = deque()
        z_add = abs(i - len(s_number) + 1)
        for j in range(len(f_number) - 1, -1, -1):
            if j == len(s_number) - 1:
                mn = 0
            last_mn = hex_dict[f_number[j]] * hex_dict[s_number[i]] + mn
            mn = last_mn // 16
            last_mn %= 16
            que.appendleft(dec_dict[last_mn])
            if j == 0 and mn != 0:
                que.appendleft(dec_dict[mn])
        for k in range(z_add):
            que.append('0')
        mn_number.append(que)
    while len(mn_number) > 1:
        mn_number[0] = add(mn_number[0], mn_number.pop())
    return mn_number

#задание списков
f_number = deque(list(input("Первое число: ").upper()))
s_number = deque(list(input("Второе число: ").upper()))
mn_number = deque()

#кодировка
hex_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,\
            '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

dec_dict = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8',\
            9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

#сложение
q_add = list(add(s_number, f_number))
print(f'{list(f_number)} + {list(s_number)} = {q_add}')

#умножение
q_mn = deque(list(*mn(s_number, f_number)))
while q_mn[0] == '0':
    q_mn.popleft()
q_mn = list(q_mn)
print(f'{list(f_number)} * {list(s_number)} = {q_mn}')

not_included = {'__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__',\
                '__builtins__', '__file__', '__cached__', 'deque', 'sys', 'show_size', 'zeroAdder', 'add', 'mn'}
local_variables_dict = locals().copy()
local_variables_dict.pop('not_included')
print(f'Список всех переменных: {local_variables_dict}')
size_of_all_variables = 0
for var in local_variables_dict.keys():
    if var not in not_included:
        size_of_all_variables += show_size(local_variables_dict[var])
print(f'Общий размер используемых переменных в программе: {size_of_all_variables} байт')


# Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
# Первое число: C4F
# Второе число: A2
# ['C', '4', 'F'] + ['0', 'A', '2'] = ['C', 'F', '1']
# ['C', '4', 'F'] * ['0', 'A', '2'] = ['7', 'C', '9', 'F', 'E']
# Список всех переменных: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000018577A51CF8>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:/DevCpp/Cource_Python_Geek/venv/Lesson_6/les_6_ver_1.py', '__cached__': None, 'deque': <class 'collections.deque'>, 'sys': <module 'sys' (built-in)>, 'show_size': <function show_size at 0x0000018577A8D268>, 'zeroAdder': <function zeroAdder at 0x0000018577D9A510>, 'add': <function add at 0x0000018577DD4268>, 'mn': <function mn at 0x0000018577DEB510>, 'f_number': deque(['C', '4', 'F']), 's_number': deque(['0', 'A', '2']), 'mn_number': deque([deque(['7', 'C', '9', 'F', 'E'])]), 'hex_dict': {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}, 'dec_dict': {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}, 'q_add': ['C', 'F', '1'], 'q_mn': ['7', 'C', '9', 'F', 'E']}
#  type=<class 'collections.deque'>, size=632, obj=deque(['C', '4', 'F'])
# 	 type=<class 'str'>, size=50, obj=C
# 	 type=<class 'str'>, size=50, obj=4
# 	 type=<class 'str'>, size=50, obj=F
#  type=<class 'collections.deque'>, size=632, obj=deque(['0', 'A', '2'])
# 	 type=<class 'str'>, size=50, obj=0
# 	 type=<class 'str'>, size=50, obj=A
# 	 type=<class 'str'>, size=50, obj=2
#  type=<class 'collections.deque'>, size=632, obj=deque([deque(['7', 'C', '9', 'F', 'E'])])
# 	 type=<class 'collections.deque'>, size=632, obj=deque(['7', 'C', '9', 'F', 'E'])
# 		 type=<class 'str'>, size=50, obj=7
# 		 type=<class 'str'>, size=50, obj=C
# 		 type=<class 'str'>, size=50, obj=9
# 		 type=<class 'str'>, size=50, obj=F
# 		 type=<class 'str'>, size=50, obj=E
#  type=<class 'dict'>, size=648, obj={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
# 	 type=<class 'str'>, size=50, obj=0
# 	 type=<class 'int'>, size=24, obj=0
# 	 type=<class 'str'>, size=50, obj=1
# 	 type=<class 'int'>, size=28, obj=1
# 	 type=<class 'str'>, size=50, obj=2
# 	 type=<class 'int'>, size=28, obj=2
# 	 type=<class 'str'>, size=50, obj=3
# 	 type=<class 'int'>, size=28, obj=3
# 	 type=<class 'str'>, size=50, obj=4
# 	 type=<class 'int'>, size=28, obj=4
# 	 type=<class 'str'>, size=50, obj=5
# 	 type=<class 'int'>, size=28, obj=5
# 	 type=<class 'str'>, size=50, obj=6
# 	 type=<class 'int'>, size=28, obj=6
# 	 type=<class 'str'>, size=50, obj=7
# 	 type=<class 'int'>, size=28, obj=7
# 	 type=<class 'str'>, size=50, obj=8
# 	 type=<class 'int'>, size=28, obj=8
# 	 type=<class 'str'>, size=50, obj=9
# 	 type=<class 'int'>, size=28, obj=9
# 	 type=<class 'str'>, size=50, obj=A
# 	 type=<class 'int'>, size=28, obj=10
# 	 type=<class 'str'>, size=50, obj=B
# 	 type=<class 'int'>, size=28, obj=11
# 	 type=<class 'str'>, size=50, obj=C
# 	 type=<class 'int'>, size=28, obj=12
# 	 type=<class 'str'>, size=50, obj=D
# 	 type=<class 'int'>, size=28, obj=13
# 	 type=<class 'str'>, size=50, obj=E
# 	 type=<class 'int'>, size=28, obj=14
# 	 type=<class 'str'>, size=50, obj=F
# 	 type=<class 'int'>, size=28, obj=15
#  type=<class 'dict'>, size=648, obj={0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
# 	 type=<class 'int'>, size=24, obj=0
# 	 type=<class 'str'>, size=50, obj=0
# 	 type=<class 'int'>, size=28, obj=1
# 	 type=<class 'str'>, size=50, obj=1
# 	 type=<class 'int'>, size=28, obj=2
# 	 type=<class 'str'>, size=50, obj=2
# 	 type=<class 'int'>, size=28, obj=3
# 	 type=<class 'str'>, size=50, obj=3
# 	 type=<class 'int'>, size=28, obj=4
# 	 type=<class 'str'>, size=50, obj=4
# 	 type=<class 'int'>, size=28, obj=5
# 	 type=<class 'str'>, size=50, obj=5
# 	 type=<class 'int'>, size=28, obj=6
# 	 type=<class 'str'>, size=50, obj=6
# 	 type=<class 'int'>, size=28, obj=7
# 	 type=<class 'str'>, size=50, obj=7
# 	 type=<class 'int'>, size=28, obj=8
# 	 type=<class 'str'>, size=50, obj=8
# 	 type=<class 'int'>, size=28, obj=9
# 	 type=<class 'str'>, size=50, obj=9
# 	 type=<class 'int'>, size=28, obj=10
# 	 type=<class 'str'>, size=50, obj=A
# 	 type=<class 'int'>, size=28, obj=11
# 	 type=<class 'str'>, size=50, obj=B
# 	 type=<class 'int'>, size=28, obj=12
# 	 type=<class 'str'>, size=50, obj=C
# 	 type=<class 'int'>, size=28, obj=13
# 	 type=<class 'str'>, size=50, obj=D
# 	 type=<class 'int'>, size=28, obj=14
# 	 type=<class 'str'>, size=50, obj=E
# 	 type=<class 'int'>, size=28, obj=15
# 	 type=<class 'str'>, size=50, obj=F
#  type=<class 'list'>, size=112, obj=['C', 'F', '1']
# 	 type=<class 'str'>, size=50, obj=C
# 	 type=<class 'str'>, size=50, obj=F
# 	 type=<class 'str'>, size=50, obj=1
#  type=<class 'list'>, size=128, obj=['7', 'C', '9', 'F', 'E']
# 	 type=<class 'str'>, size=50, obj=7
# 	 type=<class 'str'>, size=50, obj=C
# 	 type=<class 'str'>, size=50, obj=9
# 	 type=<class 'str'>, size=50, obj=F
# 	 type=<class 'str'>, size=50, obj=E
# Общий размер используемых переменных в программе: 7502 байт