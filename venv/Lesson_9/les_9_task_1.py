# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается
# не решённой.

import hashlib


def is_eq_str(a: str, b: str) -> bool:
    assert len(a) > 0 and len(b) > 0, 'Строки не могут быть пустыми'
    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()

    return ha == hb

def Rabin_Karp(s: str, subs: str) -> bool:
    assert len(s) > 0 and len(subs) > 0, 'Строки не могут быть пустыми'
    assert len(s) >= len(subs), 'Подстрока длиннее строки'
    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():

            if s[i:i + len_sub] == subs:
                return i

def sub_finder(s: str) -> int:
    assert len(s) > 0, 'Строка не должна быть пустой'

    subs_lst = []
    for i_beg in range(len(s)):
        for i_end in range(i_beg, len(s)):
            # проверка длины подстроки, чтобы не учитывать всю строку целиком
            if len(s[i_beg:i_end + 1]) < len(s):
                if Rabin_Karp(s, s[i_beg:i_end + 1]) >= 0 and s[i_beg:i_end + 1] not in subs_lst:
                    subs_lst.append(s[i_beg:i_end + 1])
    return subs_lst

s = input("Введите строку для анализа: ")
s_list = sub_finder(s)
print(f'Кол-во подстрок: {len(s_list)}\n Значение всех подстрок:\n{s_list}')
