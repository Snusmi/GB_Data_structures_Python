""""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);
проанализировать 3 варианта и выбрать оптимальный;
c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.
"""
#***********************************************
#***********************************************
#***********************************************
"""
у меня версия питон 3.7.5, ось windows 10 64 бита

Рассматриваю функции нахождения  i-го простого числа:
Решето Эратосфена. 
    Получается самый затратный по ресурсам памяти алгоритм, т.к. хранит два списка. 
    При нахождении 125го простого числа внутренние переменные функции займут почти 15 тысяч бит.
    
Нахождение просто числа через перебор делителей.
    Средний по затратам памяти. Он хранит один список.
    Для нахождения 125го простого числа внутренние переменные функции занимают почти 5 тысяч бит.

Нахождение просто числа через квадратный корень.
    Занимает меньше всего памяти, т.к. хранит всего две переменные, каждая из которых - целое число.

"""
import sys

# print(sys.platform, sys.version)
# win32 3.7.5 (default, Oct 31 2019, 15:18:51) [MSC v.1916 64 bit (AMD64)]

def show_sizeof(x, level=0):
    print("\t" * level, x.__class__, sys.getsizeof(x), x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, level + 1)
        else:
            for xx in x:
                show_sizeof(xx, level + 1)


def get_size(obj, seen=None):
    # From https://goshippo.com/blog/measure-real-size-any-python-object/
    # Recursively finds size of objects
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0

    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
      size += sum([get_size(v, seen) for v in obj.values()])
      size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
      size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
      size += sum([get_size(i, seen) for i in obj])
    return size


def sieve(n):
    end = n
    while True:
        _sieve = [i for i in range(end)] #сначала генерируем список чисел до n
        _sieve[1] = 0
        for i in range(2, end):
            if _sieve[i] != 0 :
                j = i * 2
                while j < end:
                    _sieve[j] = 0
                    j += i
        primes = [i for i in _sieve if i != 0]
        if len(primes) >= n:
            break #если длина списка с простыми числами больше или равна n - этот список подходит, т.к. в нем есть n-ое по счету простое число
        else:
            end += n #иначе увеличим исходный список чисел, например на n, и повторим цикл
    # show_sizeof(end)
    # show_sizeof(_sieve)
    # show_sizeof(primes)
    end_size = get_size(end)
    _sieve_size = get_size(_sieve)
    primes_size = get_size(primes)
    return primes[n-1], end_size + _sieve_size + primes_size

# для sieve(125)
# <class 'int'> 28 750
# <class 'list'> 6232 [список из 750 элементов], где каждый элемент занимает 24б если это 0 и 28б в остальных случаях
# <class 'list'> 1248 [список из 132 элементов], где каждый элемент занимает 28б

# print(sieve(125))
# (691, 14924)


def prime(n):
    end = n
    while True:
        primes = []
        for i in range(2, end): # генерируем список чисел от 2 до end
            for j in primes: # перебираем делители: найденные до этого простые числа (можно просто перебирать числа от 2 до i, но это еще больше увеличит время выполнения)
                if i % j == 0:
                    break
            else: # если цикл завершился без прерываний
                primes.append(i) # добавляем число в список простых чисел

        if len(primes) >= n:
            break
        else:
            end += n
    # show_sizeof(end)
    # show_sizeof(primes)
    end_size = get_size(end)
    primes_size = get_size(primes)
    return primes[n-1], end_size + primes_size

# prime(125)
# <class 'int'> 28 750
# <class 'list'> 1248 [список из 132 элементов], где каждый элемент занимает 28б

# print(prime(125))
# (691, 4972)


def prime_short(n):
    count = 1
    prime = 2

    while count < n:
        prime += 1
        for i in range(2, int(prime ** 0.5) + 1):
            if prime % i == 0:
                break
        else:
            count += 1
    # show_sizeof(count)
    # show_sizeof(prime)
    count_size = get_size(count)
    prime_size = get_size(prime)
    return prime, count_size + prime_size


# prime_short(125)
# <class 'int'> 28 125
# <class 'int'> 28 691

# print(prime_short(125))
# (691, 56)