""""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
"""

""""
Рассматривается алгоритм, который считает сумму ряда (-1/2)^n до n
* рекурсивно
* рекурсивно со словарем
* через цикл for

Цикл for работает быстрее, т.к. нет вложенных функций
"""


import cProfile

#сумма через рекурсию
def sum_recursion(n):
    return (-0.5) ** (n) + sum_recursion(n-1) if n > 0 else 1

# print(sum_recursion(6))

# "l4t1.sum_recursion(10)"
# 1000 loops, best of 5: 2.91 usec per loop

#"l4t1.sum_recursion(20)"
#1000 loops, best of 5: 5.6 usec per loop

#"l4t1.sum_recursion(50)"
#1000 loops, best of 5: 13.8 usec per loop

#"l4t1.sum_recursion(100)"
#1000 loops, best of 5: 28 usec per loop

#"l4t1.sum_recursion(500)"
#1000 loops, best of 5: 161 usec per loop

#"l4t1.sum_recursion(750)"
#1000 loops, best of 5: 236 usec per loop

# cProfile.run("sum_recursion(10)")
# 14 function calls (4 primitive calls) in 0.000 seconds
# 11/1    0.000    0.000    0.000    0.000 Lesson4_task1.py:14(sum_recursion)

# cProfile.run("sum_recursion(20)")
# 24 function calls (4 primitive calls) in 0.000 seconds
# 21/1    0.000    0.000    0.000    0.000 Lesson4_task1.py:14(sum_recursion)

# cProfile.run("sum_recursion(50)")
# 54 function calls (4 primitive calls) in 0.000 seconds
# 51/1    0.000    0.000    0.000    0.000 Lesson4_task1.py:14(sum_recursion)

# cProfile.run("sum_recursion(750)")
# 754 function calls (4 primitive calls) in 0.001 seconds
# 751/1    0.001    0.000    0.001    0.001 Lesson4_task1.py:14(sum_recursion)

#*********************************************************
#*********************************************************
#*********************************************************

#рекурсия со списком

def sum_list(n):
    sum_l = [None] * 1000
    sum_l[0] = 1

    def _sum_list(n):
        if sum_l[n] is None:
            sum_l[n] = (-0.5) ** (n) + _sum_list(n-1)
        return sum_l[n]
    return _sum_list(n)

# print(sum_list(6))

#  "l4t1.sum_list(10)"
# 1000 loops, best of 5: 9.12 usec per loop
#
# "l4t1.sum_list(20)"
# 1000 loops, best of 5: 12 usec per loop
#
#  "l4t1.sum_list(50)"
# 1000 loops, best of 5: 22.9 usec per loop
#
# "l4t1.sum_list(100)"
# 1000 loops, best of 5: 39.1 usec per loop
#
# "l4t1.sum_list(500)"
# 1000 loops, best of 5: 191 usec per loop
#
# "l4t1.sum_list(750)"
# 1000 loops, best of 5: 287 usec per loop

# cProfile.run("sum_list(10)")
# 15 function calls (5 primitive calls) in 0.000 seconds
# 11/1    0.000    0.000    0.000    0.000 Lesson4_task1.py:66(_sum_list)

# cProfile.run("sum_list(20)")
# 25 function calls (5 primitive calls) in 0.000 seconds
# 21/1    0.000    0.000    0.000    0.000 Lesson4_task1.py:66(_sum_list)

# cProfile.run("sum_list(50)")
# 55 function calls (5 primitive calls) in 0.000 seconds
# 51/1    0.000    0.000    0.000    0.000 Lesson4_task1.py:66(_sum_list)

# cProfile.run("sum_list(750)")
# 755 function calls (5 primitive calls) in 0.001 seconds
# 751/1    0.001    0.000    0.001    0.001 Lesson4_task1.py:66(_sum_list)

#*********************************************************
#*********************************************************
#*********************************************************

# сумма через цикл for

def sum_for(n):
    _sum = 0
    for i in range(n+1):
        _sum += (-0.5) ** i
    return _sum

# print(sum_for(6))

# "l4t1.sum_for(10)"
# 1000 loops, best of 5: 2.32 usec per loop
#
# "l4t1.sum_for(20)"
# 1000 loops, best of 5: 4.3 usec per loop
#
# "l4t1.sum_for(50)"
# 1000 loops, best of 5: 9.83 usec per loop
#
# "l4t1.sum_for(100)"
# 1000 loops, best of 5: 18.9 usec per loop
#
# "l4t1.sum_for(100)"
# 1000 loops, best of 5: 18.9 usec per loop
#
# "l4t1.sum_for(750)"
# 1000 loops, best of 5: 147 usec per loop

# cProfile.run("sum_for(10)")
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 Lesson4_task1.py:111(sum_for)

# cProfile.run("sum_for(20)")
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 Lesson4_task1.py:111(sum_for)

# cProfile.run("sum_for(750)")
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 Lesson4_task1.py:111(sum_for)