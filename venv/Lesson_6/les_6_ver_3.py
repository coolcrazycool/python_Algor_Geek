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

def cross_math():
    f_number = input('Первое число: ').upper()
    s_number = input('Второе число: ').upper()

    f_number = int(f_number, base=16)
    s_number = int(s_number, base=16)

    sum = f_number + s_number
    multy = f_number * s_number

    sum = str(hex(sum))
    multy = str(hex(multy))

    sum_lst = list(sum[2:].upper())
    multy_lst = list(multy[2:].upper())

    print(sum_lst)
    print(multy_lst)

    local_variables_dict = locals().copy()
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show_size(local_variables_dict[var])
    print(f'Общий размер используемых переменных в программе: {size_of_all_variables} байт')
    return 0

cross_math()


# Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
# Первое число: C4F
# Второе число: A2
# ['C', 'F', '1']
# ['7', 'C', '9', 'F', 'E']
#  type=<class 'int'>, size=28, obj=3151
#  type=<class 'int'>, size=28, obj=162
#  type=<class 'str'>, size=54, obj=0xcf1
#  type=<class 'str'>, size=56, obj=0x7c9fe
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
# Общий размер используемых переменных в программе: 806 байт