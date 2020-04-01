# Складывает и умножает 2 числа в 16-ичной системе счисления

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

def parse(num):
    num = num[::-1]
    res = 0
    i = 0
    for _ in num:
        res += hex_dict[_] * 16 ** i
        i += 1
    return res


def convert(num):
    answr = []
    cel = num
    while cel != 0:
        answr.append(dec_dict[cel % 16])
        cel = cel // 16
    return answr[::-1]


hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,\
                            'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

dec_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',\
            8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

f_number = input('Первое число: ').upper()
s_number = input('Второе число: ').upper()

f_number, s_number = parse(f_number), parse(s_number)


sum = f_number + s_number
multy = f_number * s_number

print(f'Сумма: {convert(sum)}')
print(f'Произведение: {convert(multy)}')

not_included = {'__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__',\
                '__builtins__', '__file__', '__cached__', 'deque', 'sys', 'show_size', 'parse', 'convert'}
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
# Сумма: ['C', 'F', '1']
# Произведение: ['7', 'C', '9', 'F', 'E']
# Список всех переменных: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000025A6C641CF8>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:/DevCpp/Cource_Python_Geek/venv/Lesson_6/les_6_ver_2.py', '__cached__': None, 'sys': <module 'sys' (built-in)>, 'show_size': <function show_size at 0x0000025A6C67D268>, 'parse': <function parse at 0x0000025A6C97AEA0>, 'convert': <function convert at 0x0000025A6C98A048>, 'hex_dict': {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}, 'dec_dict': {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}, 'f_number': 3151, 's_number': 162, 'sum': 3313, 'multy': 510462}
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
#  type=<class 'int'>, size=28, obj=3151
#  type=<class 'int'>, size=28, obj=162
#  type=<class 'int'>, size=28, obj=3313
#  type=<class 'int'>, size=28, obj=510462
# Общий размер используемых переменных в программе: 3896 байт