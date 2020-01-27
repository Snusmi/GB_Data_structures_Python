""""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается нерешённой.
"""

import hashlib

def count_subsrtings(a:str)->int:
    len_a = len(a)
    substrings = set([])

    for i in range(1, len_a):
        for k in range(len_a + 1 - i):
            substrings.add(hashlib.sha1(a[k:k + i].encode('utf-8')).hexdigest())
    return len(substrings)


string = input('Введите строку: ')
green = '\033[92m'
end = '\033[0m'
print(f'В строке "{green + string + end}" содержится {count_subsrtings(string)} уникальных подстрок')