""""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена». Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""

""""
Решето эратосфена выполняется быстрее
"""

import cProfile

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
    return primes[n-1]

# print(sieve(30))

# "l4t2.sieve(10)"
# 1000 loops, best of 5: 12.8 usec per loop

# "l4t2.sieve(20)"
# 1000 loops, best of 5: 44.4 usec per loop

# "l4t2.sieve(50)"
# 1000 loops, best of 5: 164 usec per loop

# "l4t2.sieve(100)"
# 1000 loops, best of 5: 498 usec per loop

# "l4t2.sieve(500)"
# 1000 loops, best of 5: 5.04 msec per loop

#  "l4t2.sieve(1000)"
# 1000 loops, best of 5: 10.4 msec per loop

# cProfile.run("sieve(10)")
# 13 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 Lesson4_task2.py:14(sieve)
# 3    0.000    0.000    0.000    0.000 Lesson4_task2.py:17(<listcomp>)
# 3    0.000    0.000    0.000    0.000 Lesson4_task2.py:25(<listcomp>)
# 3    0.000    0.000    0.000    0.000 {built-in method builtins.len}

# cProfile.run("sieve(50)")
# 19 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 Lesson4_task2.py:14(sieve)
# 5    0.000    0.000    0.000    0.000 Lesson4_task2.py:17(<listcomp>)
# 5    0.000    0.000    0.000    0.000 Lesson4_task2.py:25(<listcomp>)
# 5    0.000    0.000    0.000    0.000 {built-in method builtins.len}

# cProfile.run("sieve(100)")
# 22 function calls in 0.001 seconds
# 1    0.000    0.000    0.000    0.000 Lesson4_task2.py:14(sieve)
# 6    0.000    0.000    0.000    0.000 Lesson4_task2.py:17(<listcomp>)
# 6    0.000    0.000    0.000    0.000 Lesson4_task2.py:25(<listcomp>)
# 6    0.000    0.000    0.000    0.000 {built-in method builtins.len}

# cProfile.run("sieve(1000)")
# 28 function calls in 0.010 seconds
# 1    0.008    0.008    0.010    0.010 Lesson4_task2.py:14(sieve)
# 8    0.001    0.000    0.001    0.000 Lesson4_task2.py:17(<listcomp>)
# 8    0.001    0.000    0.001    0.000 Lesson4_task2.py:25(<listcomp>)
# 8    0.000    0.000    0.000    0.000 {built-in method builtins.len}


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
    return primes[n-1]

# print(prime(30))

# "l4t2.prime(10)"
# 1000 loops, best of 5: 10.1 usec per loop

# "l4t2.prime(20)"
# 1000 loops, best of 5: 40.8 usec per loop

# "l4t2.prime(50)"
# 1000 loops, best of 5: 229 usec per loop

# "l4t2.prime(100)"
# 1000 loops, best of 5: 950 usec per loop

# "l4t2.prime(500)"
# 1000 loops, best of 5: 29.3 msec per loop

# cProfile.run("prime(10)")
# 29 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 Lesson4_task2.py:81(prime)
# 22    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run("prime(50)")
# 183 function calls in 0.001 seconds
# 1    0.001    0.001    0.001    0.001 Lesson4_task2.py:81(prime)
# 174    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run("prime(100)")
# 425 function calls in 0.009 seconds
# 1    0.008    0.008    0.009    0.009 Lesson4_task2.py:81(prime)
# 415    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run("prime(500)")
# 2653 function calls in 0.197 seconds
# 1    0.197    0.197    0.197    0.197 Lesson4_task2.py:81(prime)
# 2641    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}